"""
@author: Argert Boja
@org: ABEnt
@date: May 2019
@description: parent class for all towers which will be created
"""

# import packages
import pygame
import math
import time
import os
from tower_defense.menu.menu import Menu

# load tower menu image
menu_bg = pygame.transform.scale(pygame.image.load(os.path.join("tower_defense\imgs\menu", "bg.png")),(160, 50))

class Tower:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.buy_costs = [0,0,0]
        self.upgrade_price = [0,0,0]
        self.level = 1
        self.selected = False
        self.menu = Menu(self, self.x, self.y, menu_bg, [])
        self.imgs = []
        self.img = None
        self.animation_count = 0
        self.timer = time.time()
        self.damage = 1
        self.range = 1
        self.value = []

    def click(self, x_pos, y_pos):
        """
        Returns if tower was clicked and if so, selects it
        :param x_pos: int
        :param y_pos: int
        :return: bool
        """
        if self.img is not None:
            if x_pos >= self.x and x_pos <= (self.x + self.img.get_width()):
                if y_pos >= self.y and y_pos <= (self.y + self.img.get_height()):
                    return True

        return False

    def attack(self, enemies, range, inRange, damage, hit_image_count):
        """
        Decides whether the tower should start attacking
        :param enemies: list of enemies
        :return: None
        """
        self.in_range = False
        closest_enemies = []
        for enemy in enemies:
            if self.img is not None:
                dis = math.sqrt((int(self.x + (self.img.get_width() / 2)) - enemy.x)**2 + (int(self.y + (self.img.get_height() / 2)) - enemy.y)**2)
                if dis < self.range:
                    self.in_range = True
                    closest_enemies.append(enemy)

        closest_enemies.sort(key=lambda x: x.x)
        if len(closest_enemies) > 0:
            closest_enemy = closest_enemies[0]
            if self.animation_count == hit_image_count:
                if closest_enemy.hit(damage):
                    enemies.remove(closest_enemy)
                    return closest_enemy.max_health
        return 0
