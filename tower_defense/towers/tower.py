import pygame

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