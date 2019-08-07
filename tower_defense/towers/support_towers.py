"""
@author: Argert Boja
@org: ABEnt
@date: May 2019
@description: Support tower class
"""
# import packages
import pygame
import os
import math
from .tower import Tower

# load images
upgrade_img = pygame.transform.scale(pygame.image.load(os.path.join("tower_defense\imgs\menu", "upgrade.png")),(32, 32))
sell_img = pygame.transform.scale(pygame.image.load(os.path.join("tower_defense\imgs\menu", "sell.png")),(32, 32))
imgs = [[pygame.transform.scale(pygame.image.load(os.path.join("tower_defense\imgs\\towers\support_towers", "tower1_level1_damage.png")), (80, 80)),
                     pygame.transform.scale(pygame.image.load(os.path.join("tower_defense\imgs\\towers\support_towers", "tower1_level2_damage.png")), (80, 80)),
                     pygame.transform.scale(pygame.image.load(os.path.join("tower_defense\imgs\\towers\support_towers", "tower1_level3_damage.png")), (80, 80))],
                    [pygame.transform.scale(pygame.image.load(os.path.join("tower_defense\imgs\\towers\support_towers", "tower2_level1_damage.png")), (80, 80)),
                     pygame.transform.scale(pygame.image.load(os.path.join("tower_defense\imgs\\towers\support_towers", "tower2_level2_damage.png")), (80, 80)),
                     pygame.transform.scale(pygame.image.load(os.path.join("tower_defense\imgs\\towers\support_towers", "tower2_level3_damage.png")), (80, 80))],
                    [pygame.transform.scale(pygame.image.load(os.path.join("tower_defense\imgs\\towers\support_towers", "tower3_level1_damage.png")), (80, 80)),
                     pygame.transform.scale(pygame.image.load(os.path.join("tower_defense\imgs\\towers\support_towers", "tower3_level2_damage.png")), (80, 80)),
                     pygame.transform.scale(pygame.image.load(os.path.join("tower_defense\imgs\\towers\support_towers", "tower3_level3_damage.png")), (80, 80))]]

class RangeTower(Tower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y
        self.id = 3
        self.ranges = [0.1, 0.3, 0.5]
        self.level = 1
        self.range = 128
        self.img = None
        self.menu.set_position(self.x - 15, self.y + 120)
        self.menu.set_cost([1000, 3000, "MAX"])
        self.value = [30, 100, 300]
        self.menu.add_button(upgrade_img, "Upgrade")
        self.menu.add_button(sell_img, "Sell")


    def draw(self, win, paused):
        """
        Draw tower images
        :param win: Surface
        :return: None
        """
        self.img = imgs[0][0]

        surface = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
        pygame.draw.circle(surface, (120, 120, 120, 100),
                           (self.range, self.range),
                           self.range, self.range)
        if self.selected:
            win.blit(surface, (
        int(self.x + (self.img.get_width() / 2) - self.range), int(self.y + (self.img.get_height() / 2) - self.range)))
            self.menu.draw(win)
        win.blit(self.img, (self.x, self.y))

    def increase_range(self, towers):
        """
        Increase range of towers that are affected
        :param towers:
        :return:
        """
        for t in towers:
            dis = math.sqrt((int(self.x ) - t.x) ** 2 + (
                        int(self.y ) - t.y) ** 2)

            if dis <= (self.range + self.width / 2):
                t.range = t.original_range + round(t.range * self.ranges[self.level - 1])

    def upgrade(self):
        """
        Upgrade support tower by increasing range
        :return: None
        """
        if self.level < 3:
            self.level += 1
            self.range += 50