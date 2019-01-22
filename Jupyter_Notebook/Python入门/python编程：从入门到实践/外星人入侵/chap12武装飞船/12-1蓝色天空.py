import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((500, 300))
pygame.display.set_caption("蓝色天空")
image = pygame.image.load("蓝色天空.png")
rect = image.get_rect()
rect.topleft = (0, 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.blit(image, rect)
    pygame.display.flip()


