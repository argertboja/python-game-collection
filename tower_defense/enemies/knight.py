import pygame
import os
from .enemy import Enemy

imgs = []
for x in range(1, 7):
    imgs.append(pygame.transform.scale(
        pygame.image.load(os.path.join("tower_defense\imgs\enemies\knight", "Knight_walk_0" + str(x) + ".png")),
        (64, 64)))

class Knight(Enemy):

    def __init__(self):
        super().__init__()
        self.max_health = 80
        self.health = self.max_health
        self.imgs = imgs[:]



