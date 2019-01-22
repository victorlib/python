import sys
import pygame
from pygame.sprite import Sprite
from pygame.sprite import Group


class Bullet(Sprite):
    def __init__(self, screen, ship):
        super().__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 15, 3)
        self.rect.centery = ship.rect.centery
        self.rect.right = ship.rect.right

    def update(self):
        self.rect.x += 3

    def draw(self):
        pygame.draw.rect(self.screen, (60, 60, 60), self.rect)


class Ship:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("ship.png")
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.moving_top = False
        self.moving_bottom = False
        self.rect.left = 0
        self.rect.centery = self.screen_rect.centery

    def update(self):
        if self.moving_top and self.rect.top > 0:
            self.rect.centery -= 1
        if self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class Alien(Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('alien.png')
        self.direction = 1
        self.rect = self.image.get_rect()
        self.rect.x = 740
        self.rect.y = 20
        self.speed = 1     # 随命中的次数增加而增加外星人移动速度

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.top <= 0:
            return True
        elif self.rect.bottom >= screen_rect.bottom:
            return True

    def update(self):
        self.rect.y += self.direction * self.speed
        if self.check_edges():
            self.direction *= -1

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class Button:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.width, self.height = 200, 50
        self.button_color = (200, 200, 200)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.msg_image = self.font.render("Play", True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


class Status:
    def __init__(self):
        self.rest = 3      # 3次不命中则结束游戏
        self.game_active = False  # 需要点击Play按钮才能开始


def check_events(screen, ship, bullets, alien, play_button, status):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        # 退出
        if event.type == pygame.QUIT:
            sys.exit()
        # 按下上下键
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ship.moving_top = True
            elif event.key == pygame.K_DOWN:
                ship.moving_bottom = True
            elif event.key == pygame.K_SPACE:
                if status.rest > 0:
                    status.rest -= 1
                    new_bullet = Bullet(screen, ship)
                    bullets.add(new_bullet)
                else:
                    status.game_active = False
        # 松开上下键
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                ship.moving_top = False
            elif event.key == pygame.K_DOWN:
                ship.moving_bottom = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
            if button_clicked and not status.game_active:
                alien.speed = 1
                status.rest = 3
                status.game_active = True


def run_game(title, size, bg_color):
    pygame.init()
    pygame.display.set_caption(title)
    screen = pygame.display.set_mode(size)
    ship = Ship(screen)
    alien = Alien(screen)
    bullets = Group()
    play_button = Button(screen)
    status = Status()
    while True:
        check_events(screen, ship, bullets, alien, play_button, status)
        screen.fill(bg_color)
        ship.blitme()
        alien.blitme()
        if status.game_active:
            ship.update()
            alien.update()
            bullets.update()
            # 检查子弹和飞船之间的碰撞
            if pygame.sprite.spritecollide(alien, bullets, True):
                alien.speed += 1
                status.rest += 1
            for bullet in bullets.copy():
                if bullet.rect.left >= 800:
                    bullets.remove(bullet)
            for bullet in bullets.sprites():
                bullet.draw()
        else:
            play_button.draw_button()
        pygame.display.flip()


def main():
    title = "有一定难度的射击练习"
    size = (800, 600)
    bg_color = (0, 0, 0)
    run_game(title, size, bg_color)


main()
