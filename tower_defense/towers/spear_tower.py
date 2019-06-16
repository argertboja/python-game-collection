import pygame
import os

from .tower import Tower

class SpearTower(Tower):

    def __init__(self):
        super().__init__()
        self.imgs = []

        for x in range(1,18):
            if self.level == 1:
                self.imgs.append(pygame.transform.scale(
                    pygame.image.load(os.path.join("tower_defense\imgs\\towers\\tower1_level1","t" + str(x) + ".png")),
                    (88, 176)))
            elif self.level == 2:
                self.imgs.append(pygame.transform.scale(
                    pygame.image.load(os.path.join("tower_defense\imgs\\towers\\tower1_level2", "t" + str(x) + ".png")),
                    (88, 176)))
            elif self.level == 3:
                self.imgs.append(pygame.transform.scale(
                    pygame.image.load(os.path.join("tower_defense\imgs\\towers\\tower1_level3", "t" + str(x) + ".png")),
                    (88, 176)))
