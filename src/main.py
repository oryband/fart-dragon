#!/usr/bin/env python
# encoding: utf8

import sys
from math import copysign

import pygame
# TODO: Fix flake8 error
from pygame.locals import K_SPACE, K_ESCAPE


BLACK = pygame.Color('black')
RES = (800, 600)
TICK = 30
X_INIT, Y_ROOF, Y_FLOOR = 50, 50, RES[1] -50
MAX_SPEED = 13
ACC = 2


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


def render(dragon, x, y):
    screen.fill(BLACK)
    screen.blit(dragon, (x, y))
    pygame.display.flip()


def load_images(images):
    # TODO: error handeling (copy from chimp tut).
    im_list = []
    for im in images:
        im_list.append(pygame.image.load(im))

    return im_list


if __name__ == '__main__':
    # Init.
    screen = pygame.display.set_mode(RES)
    clock = pygame.time.Clock()
    pygame.key.set_repeat(0, 5)

    images = load_images(('dragon.png',))
    dragon = images[0]

    x, y = X_INIT, Y_ROOF
    speed = 0

    screen.blit(dragon, (x, y))
    pygame.display.flip()

    # Game loop.
    while True:
        clock.tick(TICK)
        acc = input(pygame.event.get())
        y, speed = simulation(y, speed, acc)
        render(dragon, x, y)
