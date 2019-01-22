import sys
import pygame


def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            print(event.key)


def run_game(title, size, bg_color):
    pygame.init()
    pygame.display.set_caption(title)
    screen = pygame.display.set_mode(size)

    while True:
        check_events()
        screen.fill(bg_color)
        pygame.display.flip()


title = "按键"
size = (800, 600)
bg_color = (0, 0, 0)
run_game(title, size, bg_color)