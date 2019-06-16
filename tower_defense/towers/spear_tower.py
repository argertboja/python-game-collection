import pygame
import os
import math

from .tower import Tower

class SpearTower(Tower):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.imgs = []
        self. range = 300
        self.in_range = False

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

    def change_range(self, new_range):
        """
        Change the shoting range of a tower
        :param new_range:
        :return:
        """
        self.range = new_range

    def attack(self, enemies):
        self.in_range = False
        for enemy in enemies:
            dis = math.sqrt((self.x - enemy.x)**2 + (self.y - enemy.y)**2)
            if dis < self.range:
                self.in_range = True

    def draw(self, win):
        self.img = self.imgs[self.animation_count // 4]

        if self.in_range == False:
            self.animation_count = 0
        else:
            self.animation_count += 1
            if self.animation_count >= len(self.imgs) * 4:
                self.animation_count = 0

        win.blit(self.img, (self.x, self.y))