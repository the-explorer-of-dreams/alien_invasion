#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pygame.font

class ScoreBoard:
    """显示得分信息的类"""

    def __init__(self, ai_settings, screen, stats):
        """初始化显示得分涉及的属性"""
        self.screen =screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # 显示得分信息时使用的字体设置
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # 准备初始化得分图像
        self.prep_score()

    def prep_score(self):
        """Render the score digit into an image"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True
                                            , self.text_color, self.ai_settings.background_color)

        # 将得分放到屏幕右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """在屏幕上显示得分"""
        self.screen.blit(self.score_image, self.score_rect)