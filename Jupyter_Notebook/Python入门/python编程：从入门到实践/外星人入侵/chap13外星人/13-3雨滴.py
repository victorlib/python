import sys
import pygame
from pygame.sprite import Sprite
from pygame.sprite import Group


class Raindrop(Sprite):
    """表示单个雨滴的类"""
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Raindrop_16px.png')
        self.rect = self.image.get_rect()

    def update(self):
        """向下移动雨滴"""
        self.rect.y += 2


def create_raindrops(raindrops):
    """创建雨滴群"""
    for i in range(10):
        for j in range(38):
            raindrop = Raindrop()
            raindrop.rect.x = j * raindrop.rect.width * 1.2 + 30
            raindrop.rect.y = i * raindrop.rect.height * 1.2 + 30
            raindrops.add(raindrop)


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("雨滴")

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
            if raindrop.rect.y > 550:
                raindrops.remove(raindrop)

main()
