import sys
import pygame
from pygame.sprite import Sprite
from pygame.sprite import Group


class Bullet(Sprite):
    def __init__(self, screen, rocket):
        """在飞船所处的位置创建一个子弹对象"""
        super().__init__()
        self.screen = screen

        # 在(0,0)处创建一个表示子弹的矩形，再设置正确位置
        self.rect = pygame.Rect(0, 0, 15, 3)
        self.rect.centery = rocket.rect.centery
        self.rect.right = rocket.rect.right

    def update(self):
        """向右移动子弹"""
        self.rect.x += 1

    def draw(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, (60, 60, 60), self.rect)


class Rocket:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("火箭2.png")
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


def check_events(screen, rocket, bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        # 退出
        if event.type == pygame.QUIT:
            sys.exit()
        # 按下上下键
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                rocket.moving_top = True
            elif event.key == pygame.K_DOWN:
                rocket.moving_bottom = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, rocket)
                bullets.add(new_bullet)

        # 松开上下键
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                rocket.moving_top = False
            elif event.key == pygame.K_DOWN:
                rocket.moving_bottom = False


def run_game(title, size, bg_color):
    pygame.init()
    pygame.display.set_caption(title)
    screen = pygame.display.set_mode(size)
    rocket = Rocket(screen)
    bullets = Group()

    while True:
        check_events(screen, rocket, bullets)
        screen.fill(bg_color)
        rocket.update()
        rocket.blitme()
        bullets.update()
        for bullet in bullets.copy():
            if bullet.rect.left >= 800:
                bullets.remove(bullet)
        for bullet in bullets.sprites():
            bullet.draw()
        pygame.display.flip()


title = "侧面射击"
size = (800, 600)
bg_color = (0, 0, 0)
run_game(title, size, bg_color)

