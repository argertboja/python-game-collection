import pygame
import os

star_img = pygame.transform.scale(pygame.image.load(os.path.join("tower_defense\imgs\menu", "star.png")),(16, 16))

class Button:
    def __init__(self, x, y, img, name):
        self.name = name
        self.x = x
        self.y = y
        self.img = img
        self.width = self.img.get_width()
        self.height = self.img.get_height()

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))
        win.blit(star_img, (self.x + 40, self.y))

    def click(self, x, y):
        if x >= self.x and x <= self.x + self.width:
            if y >= self.y and y <= self.y + self.height:
                return True
        return False

pygame.font.init()

class Menu:
    def __init__(self, tower, x, y, bg, item_cost):
        self.item_cost = item_cost
        self.tower = tower
        self.x = x
        self.y = y
        self.width = 0
        self.height = 0
        self.buttons = []
        self.items = 0
        self.bg = bg
        self.font = pygame.font.SysFont("comicsans", 20)


    def draw(self, win):
        win.blit(self.bg, (self.x, self.y - self.bg.get_height()))
        for button in self.buttons:
            button.draw(win)
            text = self.font.render(str(self.item_cost[self.tower.level - 1]), 1, (255,255,255))
            win.blit(text, (self.x + 50, self.y - 20) )
            text2 = self.font.render(str(self.tower.value[self.tower.level - 1]), 1, (255, 255, 255))
            win.blit(text2, (self.x + 115, self.y - 20))


    def clicked(self, x, y):
        for button in self.buttons:
            if button.click(x, y):
                return button.name

    def add_button(self, img, name):
        if self.items == 0:
            button_x = self.x + 15
            button_y = self.y - 40
            self.items += 1
            button = Button(button_x, button_y, img, name)
            self.buttons.append(button)
        else:
            button_x = self.buttons[len(self.buttons) - 1].x + 65
            button_y = self.y - 42
            self.items += 1
            button = Button(button_x, button_y, img, name)
            self.buttons.append(button)

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def set_cost(self, item_cost):
        self.item_cost = item_cost


