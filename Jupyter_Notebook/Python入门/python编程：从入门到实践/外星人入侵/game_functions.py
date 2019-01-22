import sys
import pygame
import json
from 外星人入侵.bullet import Bullet
from 外星人入侵.alien import Alien
from time import sleep


def store_max_score(filename, num):
    with open(filename, 'w') as file_obj:
        json.dump(num, file_obj)


def fire_bullet(settings, screen, ship, bullets):
    """如果还没有到达限制， 就发射一颗子弹"""
    if len(bullets) < settings.bullet_allowed:
        new_bullets = Bullet(settings, screen, ship)
        bullets.add(new_bullets)


def check_keydown_events(event, settings, screen, stats, sb, ship, aliens, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        store_max_score(settings.max_score_file, stats.high_score)
        sys.exit()
    elif event.key == pygame.K_p and not stats.game_active:
        start_game(settings, screen, stats, sb, ship, aliens, bullets)


def check_events(settings, screen, stats, sb, ship, aliens, bullets, play_button):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        # 退出
        if event.type == pygame.QUIT:
            store_max_score(settings.max_score_file, stats.high_score)
            sys.exit()
        # 按下左右键
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, stats, sb, ship, aliens, bullets)
        # 松开左右键
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False
        # 鼠标单击
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)


def start_game(settings, screen, stats, sb, ship, aliens, bullets):
    # 清空外星人列表和子弹列表
    aliens.empty()
    bullets.empty()
    # 隐藏光标
    pygame.mouse.set_visible(False)
    # 重置游戏设置
    settings.initialize_dynamic_settings()
    # 重置游戏统计信息
    stats.reset_stats()
    stats.game_active = True
    # 开始生命值减一，修复第二局游戏开始会自动减一的bug
    if stats.one:
        stats.ships_left -= 1
        stats.one = False

    # 重置记分牌图像
    sb.prep_score()
    sb.prep_high_score()
    sb.prep_level()
    sb.prep_ships()

    # 创建一群新的外星人，并让飞船居中
    create_fleet(settings, screen, ship, aliens)
    ship.center_ship()


def check_play_button(settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """在玩家单击play按钮时开始游戏"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        start_game(settings, screen, stats, sb, ship, aliens, bullets)


def update_bullets(settings, screen, stats, sb, ship, aliens, bullets):
    """更新子弹的位置，并删除已经消失的子弹"""
    # 更新子弹的位置
    bullets.update()

    # 删除已经消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(settings, screen, stats, sb, ship, aliens, bullets)


def check_bullet_alien_collisions(settings, screen, stats, sb, ship, aliens, bullets):
    if len(aliens) == 0:
        # 删除现有的子弹, 加快游戏节奏，并新建一群外星人
        bullets.empty()
        settings.increase_speed()
        # 提高等级
        sb.prep_level()
        stats.level += 1
        create_fleet(settings, screen, ship, aliens)

    # 检查是否有子弹击中外星人，如果是这样就删除相应的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    # 要模拟能够穿行到屏幕顶端的高能子弹——消灭它击中的每个外星人， 可将第一个布尔实参设置
    # 为False ， 并让第二个布尔实参为True 。 这样被击中的外星人将消失， 但所有的子弹都始终有效， 直到抵达屏幕顶端后消失。
    if collisions:
        sb.prep_score()
        check_high_score(stats, sb)
        stats.score += settings.alien_points


def ship_hit(settings, stats, sb, screen, ship, aliens, bullets):
    """响应被外星人撞到的飞船"""
    if stats.ships_left > 0:
        stats.ships_left -= 1
        sb.prep_ships()
        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()
        # 创建一群新的外星人，并将飞船放到屏幕底部中央
        create_fleet(settings, screen, ship, aliens)
        ship.center_ship()
        # 暂停
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_aliens_bottom(settings, stats, sb, screen, ship, aliens, bullets):
    """检查是否有外星人到达了屏幕底部"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(settings, stats, sb, screen, ship, aliens, bullets)
            break


def check_high_score(stats, sb):
    """检查是否诞生了新的最高得分"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()


def update_aliens(settings, stats, sb, screen, ship, aliens, bullets):
    """
    检查是否有外星人达到屏幕边缘
    然后更新所有外星人的位置
    """
    check_fleet_edges(settings, aliens)
    # 检查外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(settings, stats, sb, screen, ship, aliens, bullets)
    else:
        # 检查是否有外星人到达屏幕底端
        check_aliens_bottom(settings, stats, sb, screen, ship, aliens, bullets)
    aliens.update()


def update_screen(settings, screen, stats, sb, ship, aliens, bullets, play_button):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(settings.bg_color)
    # 显示得分
    sb.show_score()
    # 绘制子弹,飞船，外星人
    if len(bullets):
        for bullet in bullets.sprites():
            bullet.draw()
    ship.blitme()
    if len(aliens):
        aliens.draw(screen)

    # 如果游戏处于非活动状态，就绘制play按钮
    if not stats.game_active:
        play_button.draw_button()

    # 让最近绘画的屏幕可见
    pygame.display.flip()


def get_number_aliens_x(settings, alien_width):
    """计算每行可容纳多少个外星人"""
    available_space_x = settings.screen_width - 2 * alien_width
    number_alien_x = int(available_space_x / (2 * alien_width))
    return number_alien_x


def get_number_rows(settings, ship_height, alien_height):
    """计算屏幕可容纳多少行外星人"""
    available_space_y = (settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(settings, screen, aliens, alien_number, row_number):
    """创建一个外星人并将其放在当前行"""
    alien = Alien(settings, screen)
    alien_width = alien.rect.height
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = 80 + alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(settings, screen, ship, aliens):
    """创建外星人群"""
    # 创建一个外星人，并计算一行可以容纳多少个外星人
    # 外星人间距为外星人的高度
    alien = Alien(settings, screen)
    number_alien_x = get_number_aliens_x(settings, alien.rect.height)
    number_rows = get_number_rows(settings, ship.rect.height, alien.rect.height)

    for row_number in range(number_rows):
        for alien_number in range(number_alien_x):
            create_alien(settings, screen, aliens, alien_number, row_number)


def check_fleet_edges(settings, aliens):
    """有外星人到达边缘时采取相应的措施"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(settings, aliens)
            break


def change_fleet_direction(settings, aliens):
    """将整群外星人下移， 并改变它们的方向"""
    for alien in aliens.sprites():
        alien.rect.y += settings.fleet_drop_speed
    settings.fleet_direction *= -1

