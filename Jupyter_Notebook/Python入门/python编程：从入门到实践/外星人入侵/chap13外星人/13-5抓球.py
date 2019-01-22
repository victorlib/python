import sys
import pygame
from pygame.sprite import Sprite
from random import randint


class Ball(Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('ball.png')
        self.rect = self.image.get_rect()
        self.rect.x = randint(20, 760)
        self.rect.y = 10

    def update(self):
        self.rect.y += 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class Player(Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('hand.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)


def check_events(player):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # 按下左右键
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.moving_right = True
            elif event.key == pygame.K_LEFT:
                player.moving_left = True
        # 松开左右键
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player.moving_right = False
            elif event.key == pygame.K_LEFT:
                player.moving_left = False


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("抓球")
    player = Player(screen)
    ball = Ball(screen)

    while True:
        screen.fill((255, 255, 255))
        check_events(player)
        player.blitme()
        player.update()
        ball.blitme()
        ball.update()
        # 检查碰撞
        if pygame.sprite.collide_rect(ball, player) or ball.rect.y > 590:
            ball.kill()
            ball = Ball(screen)
        pygame.display.flip()


main()
