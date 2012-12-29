#!/usr/bin/env python
# encoding: utf8

from renderer import RES

import pygame

from math import copysign


X_INIT, Y_ROOF, Y_FLOOR = 50, 50, RES[1] - 90
MAX_SPEED = 8
ACC = 1


# TODO: Create `objects` dict with objects{images:x, x:, y:, etc.:}
# `objects` will be passed to simulator, renderer, etc.
def simulation(objects, y, speed, acc=ACC):
    d = objects['dragon']
    d['speed'] += acc

    if abs(d['speed']) > MAX_SPEED:
        sign = int(copysign(1, d['speed']))  # sign = [+-]1
        d['speed'] = sign * MAX_SPEED

    new_y = d['y'] + speed

    if new_y < Y_ROOF:
        new_y = Y_ROOF
        speed = 0
    elif new_y > Y_FLOOR:
        new_y = Y_FLOOR
        speed = 0

    return new_y, speed
