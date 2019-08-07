"""
@author: Argert Boja
@org: ABEnt
@date: May 2019
@description: Village tower class
"""

# import packages
import pygame
import os
from .tower import Tower

# load images
upgrade_img = pygame.transform.scale(pygame.image.load(os.path.join("tower_defense\imgs\menu", "upgrade.png")),(32, 32))
sell_img = pygame.transform.scale(pygame.image.load(os.path.join("tower_defense\imgs\menu", "sell.png")),(32, 32))

class VillageTower(Tower):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.imgs = []
        self.imgs_level1 = []
        self.imgs_level2 = []
        self.imgs_level3 = []
        self.range = 188
        self.in_range = False
        self.flipped = False
        self.damage = 1
        self.id = 1
        self.original_range = self.range
        self.menu.set_position(self.x - 10, self.y + 175)
        self.menu.set_cost([2000, 4000, "MAX"])
        self.value = [50, 200, 400]
        self.menu.add_button(upgrade_img, "Upgrade")
        self.menu.add_button(sell_img, "Sell")

        for x in range(1,7):
            self.imgs_level1.append(pygame.transform.scale(
                pygame.image.load(os.path.join("tower_defense\imgs\\towers\\tower3_level1","" + str(x) + ".png")),
                (120, 141)))
            self.imgs_level2.append(pygame.transform.scale(
                pygame.image.load(os.path.join("tower_defense\imgs\\towers\\tower3_level2", "" + str(x) + ".png")),
                (120, 141)))
            self.imgs_level3.append(pygame.transform.scale(
                pygame.image.load(os.path.join("tower_defense\imgs\\towers\\tower3_level3", "" + str(x) + ".png")),
                (120, 141)))

        if self.level == 1:
            self.imgs = self.imgs_level1[:]
        elif self.level == 2:
            self.imgs = self.imgs_level2[:]
        elif self.level == 3:
            self.imgs = self.imgs_level3[:]


    def attack(self, enemies):
        """
        Attack enemies in given attack image number
        :param enemies: enemies
        :return: bool
        """
        return super().attack(enemies, self.range, self.in_range, self.damage, 16)

    def draw(self, win, paused):
        """
        Draw tower images
        :param win: Surface
        :param paused: paused toggle
        :return: None
        """

        self.img = self.imgs[self.animation_count // 4]

        if self.in_range == False:
            self.animation_count = 0
        else:
            if not (paused):
                self.animation_count += 1
                if self.animation_count >= len(self.imgs) * 4:
                    self.animation_count = 0

        if self.selected:
            surface = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
            pygame.draw.circle(surface, (120, 120, 120, 100),
                               (self.range, self.range),
                               self.range, self.range)
            win.blit(surface, (int(self.x + (self.img.get_width() / 2) - self.range), int(self.y + (self.img.get_height() / 2) - self.range)))
            self.menu.draw(win)
        win.blit(self.img, (self.x, self.y))

    def upgrade(self):
        """
        Upgrade tower level
        :return: None
        """
        if self.level < 3:
            self.level += 1
            self.damage += 1
            if self.level == 2:
                self.imgs = self.imgs_level2[:]
            elif self.level == 3:
                self.imgs = self.imgs_level3[:]