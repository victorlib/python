import sys
import pygame


class Rocket:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("火箭.png")
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.moving_top = False
        self.moving_right = False
        self.moving_bottom = False
        self.moving_left = False
        self.rect.center = self.screen_rect.center

    def update(self):
        if self.moving_top and self.rect.top > 0:
            self.rect.centery -= 1
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= 1
        if self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += 1
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1

    def change_direction(self, event, flag):
        if event.key == pygame.K_UP:
            self.moving_top = flag
        elif event.key == pygame.K_DOWN:
            self.moving_bottom = flag
        elif event.key == pygame.K_LEFT:
            self.moving_left = flag
        elif event.key == pygame.K_RIGHT:
            self.moving_right = flag

    def blitme(self):
        self.screen.blit(self.image, self.rect)


def check_events(rocket):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        # 退出
        if event.type == pygame.QUIT:
            sys.exit()
        # 按下上下左右键
        elif event.type == pygame.KEYDOWN:
            rocket.change_direction(event, True)

        # 松开上下左右键
        elif event.type == pygame.KEYUP:
            rocket.change_direction(event, False)


def run_game(title, size, bg_color):
    pygame.init()
    pygame.display.set_caption(title)
    screen = pygame.display.set_mode(size)
    rocket = Rocket(screen)

    while True:
        check_events(rocket)
        screen.fill(bg_color)
        rocket.update()
        rocket.blitme()
        pygame.display.flip()


title = "火箭"
size = (800, 600)
bg_color = (0, 0, 0)
run_game(title, size, bg_color)

