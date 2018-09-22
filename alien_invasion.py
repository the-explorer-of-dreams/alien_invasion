#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     alien_invasion
   Description :
   Author :       william
   date：          2018/9/19
-------------------------------------------------
   Change Activity:
                   2018/9/19:
-------------------------------------------------
"""
__author__ = 'william'

import sys
import time
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


class AlienInvasion:
    """ Alien Invasion game main class"""

    def run_game(self):
        """初始化游戏并创建一个屏幕对象"""
        pygame.init()
        pygame.display.set_caption("Alien invasion")
        ai_settings = Settings()
        screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

        # 创建一艘飞船
        ship = Ship(screen)
        # 创建一个用于存储所有子弹的编组
        bullets = Group()

        # 开始游戏主循环
        while True:
            gf.check_events(ai_settings, screen, ship, bullets)
            ship.update()
            gf.update_bullets(bullets)
            gf.update_screen(ai_settings, screen, ship, bullets)
            # time.sleep(1)

            pygame.display.flip()


if __name__ == '__main__':
    alien_invasion = AlienInvasion()
    alien_invasion.run_game()