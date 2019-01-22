import sys
import pygame
from pygame.sprite import Sprite
from pygame.sprite import Group


class Star(Sprite):
    """表示单个星星的类"""
    def __init__(self):
        """初始化星星并设置其起始位置"""
        super().__init__()
        # 加载星星图片，并设置其rect属性
        self.image = pygame.image.load('star_64px.png')
        self.rect = self.image.get_rect()


def create_stars(stars):
    """创建星星群"""
    # 5行3列
    for i in range(5):
        for j in range(8):
            star = Star()
            star.rect.x = j * star.rect.width + 20
            star.rect.y = i * star.rect.height + 20
            stars.add(star)


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("星星")

    # 创建一个星星编组
    stars = Group()
    # 创建一个星星群
    create_stars(stars)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill((0, 0, 0))
        stars.draw(screen)
        pygame.display.flip()


main()
