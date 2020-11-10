import sys
import pygame
from settings import Settings
from ship import Ship
from  alien import  Alien
import game_functions as gf
from pygame.sprite import Group
from bullet import  Bullet


def run_game():
    # 初始化pygame，设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion/外星人入侵")
    #   创建飞船
    ship = Ship(ai_settings, screen)
    alien = Alien(ai_settings,screen)
    bullets = Group()
    aliens = Group()

    #  开始创建外星群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始做游戏主循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens,  bullets )



run_game()
