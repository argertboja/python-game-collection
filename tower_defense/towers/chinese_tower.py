import pygame
import os

from .tower import Tower

class ChineseTower(Tower):

    def __init__(self):
        super().__init__()
        self.imgs = []

        for x in range(1,8):
            self.imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("tower_defense\imgs\\towers\\tower1", "t" + str(x) + ".png")), (88,176)))