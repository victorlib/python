import pygame
import json
from 外星人入侵.settings import Settings
from 外星人入侵.game_stats import GameStats
from 外星人入侵.scoreboard import Scoreboard
from 外星人入侵.button import Button
from 外星人入侵.ship import Ship
from pygame.sprite import Group
import 外星人入侵.game_functions as gf


def get_max_score(filename):
    """如果存储了最大分数， 就获取它"""
    try:
        with open(filename) as file_obj:
            num = json.load(file_obj)
    except FileNotFoundError:
        return None
    else:
        return num


def run_game():
    # 初始化pygame, Settings, 屏幕对象
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption(settings.caption)
    # 创建一艘飞船, 一个子弹编组和一个外星人编组
    ship = Ship(settings, screen)
    bullets = Group()
    aliens = Group()
    # 创建一个外星人群
    gf.create_fleet(settings, screen, ship, aliens)
    # 创建一个用于存储游戏统计信息的实例, 并创建记分牌
    stats = GameStats(settings)
    stats.ships_left -= 1
    stats.high_score = get_max_score(settings.max_score_file)
    sb = Scoreboard(settings, screen, stats)
    # 创建play按钮
    play_button = Button(settings, screen, "Play")
    # 开始游戏主循环
    while True:
        gf.check_events(settings, screen, stats, sb, ship, bullets, bullets, play_button)
        if stats.game_active:
            ship.update()
            gf.update_bullets(settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(settings, stats, sb, screen, ship, aliens, bullets)
        gf.update_screen(settings, screen, stats, sb, ship, aliens, bullets, play_button)


run_game()
