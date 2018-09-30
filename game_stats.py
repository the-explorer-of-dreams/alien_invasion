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

from game_functions import read_ini_file
from game_functions import write_ini_file
class GameStats:
    """跟踪游戏的统计信息"""

    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
        self.high_score = 0
        self.load_saved_game_status()

    def reset_stats(self):
        """初始化游戏运行期间可能变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

    def load_saved_game_status(self):
        """加载存储的游戏状态"""
        self.init_props = read_ini_file(self.ai_settings.ini_filename)
        self.high_score_saved = self.init_props['high_score']
        if self.high_score_saved:
            self.high_score = self.high_score_saved

    def save_game_status(self):
        """存储需要保存到文件的游戏状态"""
        if self.high_score > self.high_score_saved:
            self.init_props['high_score'] = self.high_score
        write_ini_file(self.ai_settings.ini_filename, self.init_props)
