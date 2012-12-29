#!/usr/bin/env python
# encoding: utf8

import pygame
from pygame.locals import RLEACCEL


MLTPLY = 71
RES = (16 * MLTPLY, 9 * MLTPLY)
BLACK = pygame.Color('black')


# Enum
class ImageType:
    BG = 0,
    PLAYER = 1


class Renderer():
    def __init__(self, screen):
        self.__images = {
            ImageType.BG: [],
            ImageType.PLAYER: []
        }

        self.__screen = pygame.display.set_mode(RES)

    def load_image(self, path, tyype, color_key=None):
        try:
            image = pygame.image.load(path)
        except pygame.error:
            print 'Cannot load image:', path
            raise

        image = image.convert()

        if color_key is not None:
            if color_key is -1:
                color_key = image.get_at((0, 0))
            image.set_color_key(color_key, RLEACCEL)

        self.__images[tyype].append({
            'image': image,
            'x': 0,
            'y': 0
        })

        return self.__images[tyype][-1]

    def render(self):
        self.__screen.fill(BLACK)

        bg_1 = self.__images[ImageType.BG]
        bg_2 = self.__images[ImageType.BG]

        if bg_1['x'] <= -1 * bg_1.get_width():
            bg_1['x'] = bg_2['x'] + bg_2.get_width()

        if bg_2['x'] <= -1 * bg_2.get_width():
            bg_2['x'] = bg_1['x'] + bg_1.get_width()

        for o in self.__images[ImageType.PLAYER]:
            self.__screen.blit(o['image'], (o['x'], o['y']))

        pygame.display.flip()
