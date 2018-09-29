#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     game_stats
   Description :
   Author :       william
   date：          2018/9/29
-------------------------------------------------
   Change Activity:
                   2018/9/29:
-------------------------------------------------
"""
__author__ = 'william'


class GameStats:
    """跟踪游戏的统计信息"""

    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()

    def reset_stats(self):
        """初始化游戏运行期间可能变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit