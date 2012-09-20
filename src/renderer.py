#!/usr/bin/env python
# encoding: utf8

import pygame
from pygame.locals import RLEACCEL


BLACK = pygame.Color('black')


class ImageType:
    BG = 0,
    PLAYER = 1


class Renderer():
    def __init__(self, screen):
        self.__images = {
            ImageType.BG: [],
            ImageType.PLAYER: []
        }

        self.__screen = screen

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

        for i in self.__images[ImageType.BG]:
            self.__screen.blit(i)

        for o in self.__images[ImageType.PLAYER]:
            self.__screen.blit(o['image'], (o['x'], o['y']))

        pygame.display.flip()
