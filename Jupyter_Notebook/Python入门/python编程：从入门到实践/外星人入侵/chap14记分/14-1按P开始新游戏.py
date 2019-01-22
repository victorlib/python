# 修改部分
def check_play_button(settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """提取了if语句下的所有代码，放到start_game()中"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        start_game(settings, screen, stats, ship, aliens, bullets)


def start_game(settings, screen, stats, ship, aliens, bullets):
    """将check_play_button() 的一些代码提取出来"""
    # 隐藏光标
    pygame.mouse.set_visible(False)

    # 重置游戏统计信息
    stats.reset_stats()
    stats.game_active = True

    # 清空外星人列表和子弹列表
    aliens.empty()
    bullets.empty()

    # 创建一群新的外星人，并让飞船居中
    create_fleet(settings, screen, ship, aliens)
    ship.center_ship()


def check_keydown_events(event, settings, screen, stats, ship, aliens, bullets):
    """添加了参数stats, aliens，并加入判断当按下p时且游戏为非活跃状态时开始游戏"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_p and not stats.game_active:
        start_game(settings, screen, stats, ship, aliens, bullets)
