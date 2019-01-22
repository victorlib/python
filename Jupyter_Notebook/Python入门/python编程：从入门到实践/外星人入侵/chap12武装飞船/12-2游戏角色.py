import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((500, 300))
pygame.display.set_caption("游戏角色")
image = pygame.image.load("悟空.png")
rect = image.get_rect()
rect.center = (250, 150)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.blit(image, rect)
    pygame.display.flip()

