#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     settings
   Description :
   Author :       william
   date：          2018/9/19
-------------------------------------------------
   Change Activity:
                   2018/9/19:
-------------------------------------------------
"""
__author__ = 'william'


class Settings:
    """存储所有《外星人入侵》的所有配置"""

    def __init__(self):
        """初始化游戏的静态设置"""
        # 屏幕设置
        self.screen_width = 900
        self.screen_height = 600
        self.background_color = (230, 230, 230)

        # 飞船的设置
        self.ship_limit = 3

        # 子弹设置
        self.bullet_width = 300
        self.bullet_height = 12
        self.bullet_color = (90, 90, 90)
        self.bullets_allowed = 3

        # 外星人设置
        self.fleet_drop_speed = 80


        # 加快游戏节奏的速度因子
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed_factor = 2
        self.bullet_speed_factor = 2
        self.alien_speed_factor = 1

        # fleet_direction为1表示向右移，-1表示向左移
        self.fleet_direction = 1

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
