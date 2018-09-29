#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


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


def check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """在玩家单击play按钮时开始新游戏"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # 重置游戏设置
        ai_settings.initialize_dynamic_settings()
        # 隐藏光标
        pygame.mouse.set_visible(False)

        # 重置游戏信息
        stats.reset_stats()
        stats.game_active = True

        # 清空外星人和子弹列表
        aliens.empty()
        bullets.empty()

        # 创建一群外星人，并让飞船居中
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


def check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y)
        elif event.type == pygame.KEYDOWN:
            # print("KEYDOWN: " + str(event.type))
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            # print("KEYDOWN: " + str(event.type))
            check_keyup_events(event, ship)


def update_screen(ai_settings, stats, score_board, screen, ship, aliens, bullets, play_button):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时更新屏幕
    screen.fill(ai_settings.background_color)
    # 绘制子弹
    for bullet in bullets:
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    score_board.show_score()
    if not stats.game_active:
        play_button.draw_button()


def check_bullet_alien_collisions(ai_settings, screen, ship, bullets, aliens):
    # 检查是否有子弹击中外星人
    # 如果有击中，删除相应的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens) == 0:
        # 删除所有子弹，并创建新的外星人编队
        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, ship, aliens)


def clear_bullets_out_of_screen(bullets):
    # 删除消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def update_bullets(ai_settings, screen, ship, bullets, aliens):
    """更新bullets，并删除已消失的子弹"""
    bullets.update()
    # 删除消失的子弹
    clear_bullets_out_of_screen(bullets)
    # 删除碰撞的子弹及外星人，全部被消灭后重新生成
    check_bullet_alien_collisions(ai_settings, screen, ship, bullets, aliens)


def fire_bullet(ai_settings, screen, ship, bullets):
    # 创建一颗子弹并加入到编组bullets中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def create_alien(ai_settings, screen, aliens, alien_width, row_number, alien_number):
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
    alien = Alien(ai_settings, screen)
    # 计算可容纳的外星人个数
    alien_width, number_aliens_x = get_number_aliens_x(ai_settings, alien)
    # 获取外星人行数
    number_rows = get_number_rows(ai_settings, alien, ship)

    # 创建外星人
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_width, row_number, alien_number)


def check_fleet_edges(ai_settings, aliens):
    """有外星人到达边缘时采取相应的措施"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """将整群外星人下移，并改变他们的移动方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def ship_hit(ai_settings, stats, screen, ship, bullets, aliens):
    """响应外星人撞到飞船"""
    if stats.ships_left > 0:
        # 将ship_left减1
        stats.ships_left -= 1

        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        # 创建一批新的外星人，并把飞船放到底部中央
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # 暂停 0.5s
        sleep(0.5)
    else:
        print(stats.game_active)
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_aliens_bottom(ai_settings, stats, screen, ship, bullets, aliens):
    """检查是否有外星人到达了屏幕底部"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # 和飞船被撞一样处理
            ship_hit(ai_settings, stats, screen, ship, bullets, aliens)
            break


def update_aliens(ai_settings, stats, screen, ship, bullets, aliens):
    """检查是否外星人位于屏幕边缘,更新外星人群的位置"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    # 检测外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        print("Ship hit!!!")
        ship_hit(ai_settings, stats, screen, ship, bullets, aliens)
    # 检测是否到达边缘
    check_aliens_bottom(ai_settings, stats, screen, ship, bullets, aliens)
