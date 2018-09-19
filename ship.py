#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     ship
   Description :
   Author :       william
   date：          2018/9/19
-------------------------------------------------
   Change Activity:
                   2018/9/19:
-------------------------------------------------
"""
__author__ = 'william'

import pygame


class Ship:
    def __init__(self, screen):
        """初始化飞船并设置"""
        self.screen = screen

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.length = self.rect.centery
        self.start_up = False
        self.screen_rect = screen.get_rect()


        # 将飞船放到屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def ship_move(self, move_step=1):
        """ 飞船向前飞行"""
        if self.start_up and (self.screen_rect.bottom - self.length == self.rect.centery):
            move_step = move_step * -1
            self.rect.centery -= move_step
        elif (self.screen_rect.bottom - self.length) >= self.rect.centery > self.length:
            self.rect.centery -= move_step
        elif self.rect.centery == self.length:
            move_step = move_step * -1
            self.rect.centery -= move_step
        else:
            pass
        self.start_up = True
        return move_step

