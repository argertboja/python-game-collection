import pygame

class Tower:

    def __init__(self):
        self.x = 50
        self.y = 50
        self.width = 0
        self.height = 0
        self.buy_costs = [0,0,0]
        self.price = [0,0,0]
        self.level = 2
        self.selected = False
        self.menu = None
        self.imgs = []
        self.img = None
        self.animation_count = 0

    def draw(self, win):
        """
        Draws tower images
        :param win: Surface
        :return: none
        """
        self.img = self.imgs[self.animation_count//4]

        self.animation_count += 1

        if self.animation_count >= len(self.imgs)*4:
            self.animation_count = 0

        win.blit(self.img, (self.x, self.y))

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
        pass

    def upgrade(self):
        pass

    def move(self):
        pass