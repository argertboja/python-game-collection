import pygame
import math
import time

class Tower:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 0
        self.height = 0
        self.buy_costs = [0,0,0]
        self.upgrade_price = [0,0,0]
        self.level = 2
        self.selected = False
        self.menu = None
        self.imgs = []
        self.img = None
        self.animation_count = 0
        self.timer = time.time()
        self.damage = 1

    def click(self, x_pos, y_pos):
        """
        Returns if tower was clicked and if so, selects it
        :param x_pos: int
        :param y_pos: int
        :return: bool
        """
        if x_pos >= self.x and x_pos <= (self.x + self.width):
            if y_pos >= self.y and y_pos <= (self.y + self.height):
                return True

        return False

    def sell(self):
        """
        returns the price of tower
        :return: int
        """
        return self.buy_costs[self.level-1]

    def upgrade(self):
        """
        Upgrades the level of tower
        :return: None
        """
        self.level += 1

    def get_uprade_cost(self):
        """
        returns the upgrade cost, and if 0 then cannot upgrade
        :return: int
        """
        return self.upgrade_price[self.level - 1]

    def move(self, x, y):
        """
        Moves the postion of the tower
        :param x: new x pos
        :param y: new y pos
        :return: none
        """
        self.x = x
        self.y = y

    def attack(self, enemies, range, inRange):
        """
        Decides whether the tower should start attacking
        :param enemies: list of enemies
        :return: None
        """
        self.in_range = False
        closest_enemies = []
        for enemy in enemies:
            dis = math.sqrt((int(self.x + (self.img.get_width() / 2)) - enemy.x)**2 + (int(self.y + (self.img.get_height() / 2)) - enemy.y)**2)
            if dis < self.range:
                self.in_range = True
                closest_enemies.append(enemy)

        closest_enemies.sort(key=lambda x: x.x)
        if len(closest_enemies) > 0:
            closest_enemy = closest_enemies[0]
            if time.time() - self.timer >= 0.5:
                self.timer = time.time()
                if closest_enemy.hit():
                    enemies.remove(closest_enemy)
            """
            This piece of code is used for archer towers in order to flip the archer
            if closest_enemy.x > self.x and not (self.flipped):
                self.flipped = True
                for x, img in enumerate(self.imgs):
                    self.imgs[x] = pygame.transform.flip(img, True, False)
            elif closest_enemy.x < self.x and self.flipped:
                self.flipped = False
                for x, img in enumerate(self.imgs):
                    self.imgs[x] = pygame.transform.flip(img, True, False)
            """