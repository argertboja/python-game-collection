import pygame
import os

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

    def click(self, x, y):
        if x >= self.x and x <= self.x + self.width:
            if y >= self.y and y <= self.y + self.height:
                return True
        return False

class Menu:
    def __init__(self, x, y, bg):
        self.x = x
        self.y = y
        self.width = 0
        self.height = 0
        self.buttons = []
        self.item_names = []
        self.items = 0
        self.bg = bg

    def draw(self, win):
        win.blit(self.bg, (self.x, self.y - self.bg.get_height()))
        for button in self.buttons:
            button.draw(win)

    def clicked(self, x, y):
        for button in self.buttons:
            if button.click(x, y):
                return button.name

    def add_button(self, img, name):
        button_x = self.items * img.get_width()
        button_y = self.y
        self.items += 1
        button = Button(button_x, button_y, img, name)
        self.buttons.append(button)

    def set_position(self, x, y):
        self.x = x
        self.y = y
