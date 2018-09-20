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
from settings import Settings

class Ship:
    def __init__(self, screen):
        """初始化飞船并设置"""
        self.screen = screen
        self.ai_settings = Settings()

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.half_length = self.rect.centery
        self.half_width = self.rect.centerx
        self.start_up = False
        self.screen_rect = screen.get_rect()

        # 将飞船放到屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 设置飞船的移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_forward = False
        self.moving_backward = False

        # 在飞船的属性center中存储小数
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def ship_move(self, move_step=1):
        """ 飞船向前飞行"""
        if self.start_up and (self.screen_rect.bottom - self.half_length == self.rect.centery):
            move_step = move_step * -1
            self.rect.centery -= move_step
        elif (self.screen_rect.bottom - self.half_length) >= self.rect.centery > self.half_length:
            self.rect.centery -= move_step
        elif self.rect.centery == self.half_length:
            move_step = move_step * -1
            self.rect.centery -= move_step
        else:
            pass
        self.start_up = True
        return move_step

    def update(self):
        """根据移动标志调整飞船位置"""
        if self.moving_right:
            if self.rect.centerx == (self.screen_rect.right - self.half_width):
                self.centerx = self.half_width
            # print(str(self.rect.centerx) + "-->" + str(self.screen_rect.right - self.half_width))
            self.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left:
            if self.rect.centerx == self.half_width:
                self.centerx = (self.screen_rect.right - self.half_width)
            self.centerx -= self.ai_settings.ship_speed_factor
        if self.moving_forward and self.rect.top > 0:
            self.centery -= self.ai_settings.ship_speed_factor
        if self.moving_backward and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.ship_speed_factor

        self.rect.centerx = self.centerx
        self.rect.centery = self.centery