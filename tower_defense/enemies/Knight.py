import pygame
import os
from .Enemy import Enemy

class Knight(Enemy):
    # imgs = [pygame.image.load(os.path.join("tower_defense\imgs\enemies\knight", "Knight_walk_0" + str(x) + ".png") for x in range(7))]
    imgs = []

    for x in range(1,7):
        imgs.append(pygame.image.load(os.path.join("tower_defense\imgs\enemies\knight", "Knight_walk_0" + str(x) + ".png" )))

    def __init__(self):
        super().__init__()
