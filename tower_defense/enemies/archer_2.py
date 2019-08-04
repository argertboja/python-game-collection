import pygame
import os
from .enemy import Enemy

imgs = []
for x in range(1, 12):
    str_to_add = str(x)
    if x < 10:
        str_to_add = "0" + str(x)
    imgs.append(pygame.transform.scale(pygame.image.load(
        os.path.join("tower_defense\imgs\enemies\\archer_2", "FantasyArcher_02_walk_00" + str_to_add + ".png")),
        (64, 64)))

class Archer_2(Enemy):

    def __init__(self):
        super().__init__()
        self.max_health = 20
        self.health = self.max_health
        self.imgs = imgs[:]



