import pygame
import os
import math

from .tower import Tower

class ArcherTower(Tower):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.imgs = []
        self.range = 100
        self.in_range = False
        self.flipped = False
        self.damage = 2
        self.id = 2
        self.original_range = self.range

        for x in range(1,7):
            if self.level == 1:
                self.imgs.append(pygame.transform.scale(
                    pygame.image.load(os.path.join("tower_defense\imgs\\towers\\tower2_level1","" + str(x) + ".png")),
                    (120, 141)))
            elif self.level == 2:
                self.imgs.append(pygame.transform.scale(
                    pygame.image.load(os.path.join("tower_defense\imgs\\towers\\tower2_level2", "" + str(x) + ".png")),
                    (120, 141)))
            elif self.level == 3:
                self.imgs.append(pygame.transform.scale(
                    pygame.image.load(os.path.join("tower_defense\imgs\\towers\\tower2_level3", "" + str(x) + ".png")),
                    (120, 141)))

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

        #pygame.draw.circle(win, (255,0,0), (int(self.x +
        #                   (self.img.get_width() / 2)), int(self.y + (self.img.get_height() / 2))), self.range, 1)
        surface = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
        pygame.draw.circle(surface, (120, 120, 120, 100),
                           (self.range, self.range),
                           self.range, self.range)
        win.blit(surface, (int(self.x + (self.img.get_width() / 2) - self.range), int(self.y + (self.img.get_height() / 2) - self.range)))
        win.blit(self.img, (self.x, self.y))