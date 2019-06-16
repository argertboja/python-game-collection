import pygame
import os

from .tower import Tower

class ChineseTower(Tower):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.imgs = []

        for x in range(1,8):
            self.imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("tower_defense\imgs\\towers\\tower1", "t" + str(x) + ".png")), (88,176)))