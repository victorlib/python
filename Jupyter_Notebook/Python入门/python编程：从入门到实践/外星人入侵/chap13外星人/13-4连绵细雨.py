import sys
import pygame
from pygame.sprite import Sprite
from pygame.sprite import Group
from random import randint


class Raindrop(Sprite):
    """表示单个雨滴的类"""
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Raindrop_32px.png')
        self.rect = self.image.get_rect()
        self.rect.y = 20

    def update(self):
        """向下移动雨滴"""
        self.rect.y += randint(1, 3)


def create_raindrops(raindrops):
    """创建雨滴群"""
    for i in range(100):
        raindrop = Raindrop()
        raindrop.rect.x = randint(20, 750)
        raindrop.rect.y = randint(20, 500)
        raindrops.add(raindrop)


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("连绵雨滴")

    raindrops = Group()
    create_raindrops(raindrops)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill((0, 0, 0))
        raindrops.draw(screen)
        raindrops.update()
        pygame.display.flip()

        for raindrop in raindrops.copy():
            if raindrop.rect.y > 590:
                raindrops.remove(raindrop)
                raindrop = Raindrop()
                raindrop.rect.x = randint(20, 750)
                raindrops.add(raindrop)



main()
