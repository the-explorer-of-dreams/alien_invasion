#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

import pygame
from bullet import Bullet
from alien import Alien


def check_keydown_events(event, ai_settings, screen, ship, bullets):
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
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

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


def check_events(ai_settings, screen, ship, bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # print("KEYDOWN: " + str(event.type))
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            # print("KEYDOWN: " + str(event.type))
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, aliens, bullets):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时更新屏幕
    screen.fill(ai_settings.background_color)
    # 绘制子弹
    for bullet in bullets:
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)


def update_bullets(bullets):
    """更新bullets，并删除已消失的子弹"""
    bullets.update()
    # 删除消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def fire_bullet(ai_settings, screen, ship, bullets):
        # 创建一颗子弹并加入到编组bullets中
        if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)


def create_alien(ai_settings, screen, aliens, alien_width, row_number,alien_number):
    # 创建外星人并加入当前行
    alien = Alien(ai_settings, screen)
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def get_number_aliens_x(ai_settings, alien):
    # 计算可容纳的外星人个数
    alien_width = alien.rect.width
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = available_space_x // (2 * alien_width)
    return alien_width, number_aliens_x


def get_number_rows(ai_settings, alien, ship):
    """ 获取外星人行数"""
    alien_height = alien.rect.height
    ship_height = ship.rect.height
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = available_space_y // (2 * alien_height)
    return number_rows


def create_fleet(ai_settings, screen, ship, aliens):
    """创建外星人群"""
    # 获取外星人的宽度
    # 计算可容纳的外星人个数
    alien = Alien(ai_settings, screen)
    alien_width, number_aliens_x = get_number_aliens_x(ai_settings, alien)
    number_rows = get_number_rows(ai_settings, alien, ship)

    # 创建第一行外星人
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_width, row_number, alien_number)
