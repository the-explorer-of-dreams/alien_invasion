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
        move_step = 1
        # 开始游戏主循环
        while True:
            for event in pygame.event.get():
                # print(event.type)
                if event.type == pygame.QUIT:
                    sys.exit()

            screen.fill(ai_settings.background_color)
            move_step = ship.ship_move(move_step)
            ship.blitme()
            # time.sleep(1)

            pygame.display.flip()


if __name__ == '__main__':
    alien_invasion = AlienInvasion()
    alien_invasion.run_game()