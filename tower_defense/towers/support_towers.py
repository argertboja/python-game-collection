import pygame
import os
import math

from .tower import Tower

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
        self.range = 100
        self.img = None


    def draw(self, win):

        self.img = imgs[self.id-1][self.level-1]

        surface = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
        pygame.draw.circle(surface, (120, 120, 120, 100),
                           (self.range, self.range),
                           self.range, self.range)
        if self.selected:
            win.blit(surface, (
        int(self.x + (self.img.get_width() / 2) - self.range), int(self.y + (self.img.get_height() / 2) - self.range)))
        win.blit(self.img, (self.x, self.y))

    def increase_range(self, towers):
        for t in towers:
            dis = math.sqrt((int(self.x ) - t.x) ** 2 + (
                        int(self.y ) - t.y) ** 2)

            if dis <= (self.range + self.width / 2) and t.id == self.id:
                t.range = t.original_range + round(t.range * self.ranges[self.level - 1])


