#!/usr/bin/env python
# encoding: utf8

from renderer import Renderer, ImageType

import pygame
# TODO: Fix flake8 error
from pygame.locals import K_SPACE, K_ESCAPE

import sys
from math import copysign


MULTIPLIER = 71
RES = (16 * MULTIPLIER, 9 * MULTIPLIER)
FPS = 60
X_INIT, Y_ROOF, Y_FLOOR = 50, 50, RES[1] - 90
MAX_SPEED = 8
ACC = 1


def input(events):
    keys = pygame.key.get_pressed()

    if keys[K_ESCAPE]:
        sys.exit(0)
    elif keys[K_SPACE]:
        return ACC
    else:
        return - ACC


def simulation(y, speed, acc):
    speed += acc

    if abs(speed) > MAX_SPEED:
        sign = int(copysign(1, speed))  # sign = [+-]1
        speed = sign * MAX_SPEED

    new_y = y + speed

    if new_y < Y_ROOF:
        new_y = Y_ROOF
        speed = 0
    elif new_y > Y_FLOOR:
        new_y = Y_FLOOR
        speed = 0

    return new_y, speed


if __name__ == '__main__':
    # Init.
    screen = pygame.display.set_mode(RES)
    clock = pygame.time.Clock()

    renderer = Renderer(screen)

    #bg_1 = renderer.load_image('background.png', ImageType.BG)
    #bg_2 = renderer.load_image('background.png', ImageType.BG)
    dragon = renderer.load_image('dragon.png', ImageType.PLAYER)

    #bg_1['x'], bg_1['y'] = 0, 0
    #bg_2['x'], bg_1['y'] = bg_1['x'].get_width(), 0
    dragon['x'], dragon['y'] = X_INIT, Y_ROOF

    speed = 0

    # Game loop.
    while True:
        clock.tick(FPS)
        acc = input(pygame.event.get())
        dragon['y'], speed = simulation(dragon['y'], speed, acc)
        renderer.render()
