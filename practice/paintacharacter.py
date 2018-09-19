#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

import pygame


def painting():
    """pygame 练习"""
    screen_size = (800, 600)
    screen = pygame.display.set_mode(screen_size)
    screen_bg_color = (255, 255, 255)
    screen.fill(screen_bg_color)

    rect_screen = screen.get_rect()
    screen_centerx = rect_screen.centerx
    screen_centery = rect_screen.centery
    monkey_image = pygame.image.load('images/mokey.bmp')
    # monkey_image.fill(screen_bg_color)
    rect_monkey_image = monkey_image.get_rect()
    print(rect_monkey_image)

    rect_monkey_image.centerx = screen_centerx
    rect_monkey_image.centery = screen_centery


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.blit(monkey_image, rect_monkey_image)
        pygame.display.flip()


if __name__ == '__main__':
    painting()