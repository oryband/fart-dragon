#!/usr/bin/env python
# encoding: utf8

from renderer import Renderer, ImageType

import pygame
# TODO: Fix flake8 error
from pygame.locals import K_SPACE, K_ESCAPE

import sys


FPS = 60

def input(events):
    keys = pygame.key.get_pressed()

    if keys[K_ESCAPE]:
        sys.exit(0)
    elif keys[K_SPACE]:
        return ACC
    else:
        return - ACC




if __name__ == '__main__':
    # Init.
    clock = pygame.time.Clock()

    renderer = Renderer(screen)

    bg_1 = renderer.load_image('background.png', ImageType.BG)
    bg_2 = renderer.load_image('background.png', ImageType.BG)
    dragon = renderer.load_image('dragon.png', ImageType.PLAYER)

    bg_1['x'], bg_1['y'] = 0, 0
    bg_2['x'], bg_1['y'] = bg_1['x'].get_width(), 0
    dragon['x'], dragon['y'] = X_INIT, Y_ROOF

    speed = 0

    # Game loop.
    while True:
        clock.tick(FPS)
        acc = input(pygame.event.get())
        dragon['y'], speed = simulation(dragon['y'], speed, acc)
        renderer.render()
