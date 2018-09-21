#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

import pygame


def check_keydown_events(event, ship):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        # 向右移动飞船
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # 向右移动飞船
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        # 向右移动飞船
        ship.moving_forward = True
    elif event.key == pygame.K_DOWN:
        # 向右移动飞船
        ship.moving_backward = True


def check_keyup_events(event, ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        # 向右移动飞船
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        # 向右移动飞船
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        # 向右移动飞船
        ship.moving_forward = False
    elif event.key == pygame.K_DOWN:
        # 向右移动飞船
        ship.moving_backward = False


def check_events(ship):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            print("KEYDOWN: " + str(event.type))
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            print("KEYDOWN: " + str(event.type))
            check_keyup_events(event, ship)


def update_screen(settings, screen, ship):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时更新屏幕
    screen.fill(settings.background_color)
    ship.blitme()