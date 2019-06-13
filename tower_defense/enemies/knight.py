import pygame
import os
from .enemy import Enemy

class Knight(Enemy):

    def __init__(self):
        super().__init__()
        # imgs = [pygame.image.load(os.path.join("tower_defense\imgs\enemies\knight", "Knight_walk_0" + str(x) + ".png") for x in range(7))]
        self.imgs = []

        for x in range(1, 7):
            self.imgs.append(pygame.transform.scale(
                pygame.image.load(os.path.join("tower_defense\imgs\enemies\knight", "Knight_walk_0" + str(x) + ".png")),
                (64, 64)))
