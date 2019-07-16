import pygame
import os
import math

from .tower import Tower

class VillageTower(Tower):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.imgs = []
        self. range = 100
        self.in_range = False
        self.flipped = False
        self.damage = 1

        for x in range(1,7):
            if self.level == 1:
                self.imgs.append(pygame.transform.scale(
                    pygame.image.load(os.path.join("tower_defense\imgs\\towers\\tower3_level1","" + str(x) + ".png")),
                    (169, 199)))
            elif self.level == 2:
                self.imgs.append(pygame.transform.scale(
                    pygame.image.load(os.path.join("tower_defense\imgs\\towers\\tower3_level2", "" + str(x) + ".png")),
                    (169, 199)))
            elif self.level == 3:
                self.imgs.append(pygame.transform.scale(
                    pygame.image.load(os.path.join("tower_defense\imgs\\towers\\tower3_level3", "" + str(x) + ".png")),
                    (169, 199)))

    def change_range(self, new_range):
        """
        Change the shoting range of a tower
        :param new_range:
        :return:
        """
        self.range = new_range

    def attack(self, enemies):
        super().attack(enemies, self.range, self.in_range, self.damage)

    def draw(self, win):
        self.img = self.imgs[self.animation_count // 4]

        if self.in_range == False:
            self.animation_count = 0
        else:
            self.animation_count += 1
            if self.animation_count >= len(self.imgs) * 4:
                self.animation_count = 0

        win.blit(self.img, (self.x, self.y))
        pygame.draw.circle(win, (255,0,0), (int(self.x + (self.img.get_width() / 2)), int(self.y + (self.img.get_height() / 2))), self.range, 1)