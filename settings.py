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
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 900
        self.screen_height = 600
        self.background_color = (230, 230, 230)

        # 飞船的设置
        self.ship_speed_factor = 2

        # 子弹设置
        self.bullet_speed_factor = 0.5
        self.bullet_width = 3
        self.bullet_height = 12
        self.bullet_color = (90, 90, 90)
        self.bullets_allowed = 3
