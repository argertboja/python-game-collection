import pygame
import os
import math

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

class VerticalButton(Button):
    def __init__(self, x, y, real_img, restricted_img, img, name, value):
        super().__init__(x, y, img, name)
        self.value = value
        self.real_img = real_img
        self.restricted_img = restricted_img

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))

    def draw_moving_button(self, win, x, y, towers, path):
        tower_collision = self.check_collision_with_tower(x, y, towers)
        path_collision = self.check_collision_with_path(x, y, path)

        return_value = True

        if tower_collision or path_collision:
            win.blit(self.restricted_img,
                     (x - self.restricted_img.get_width() / 2, y - self.restricted_img.get_height() / 2))
            return_value = False
        else:
            win.blit(self.real_img, (x - self.real_img.get_width() / 2, y - self.real_img.get_height() / 2))
            return_value = True

        return  return_value


    def check_collision_with_tower(self, x, y, towers):
        for tower in towers:
            dis = math.sqrt((x-tower.x - tower.img.get_width() / 2)**2 + (y-tower.y - tower.img.get_height() / 2)**2)
            if dis < 90:
                return True
        return False

    def check_collision_with_path(self, x, y, path):
        for position in path:
            print(position)
            dis = math.sqrt((x-position[0])**2 + (y-position[1])**2)
            if dis < 55:
                return True
        return False


class PlayPauseButton(Button):
    def __init__(self, x, y, img, play_img, pause_img):
        super().__init__(x, y, img, "")
        self.play_img = play_img
        self.pause_img = pause_img
        self.paused = False

    def draw(self, win):
        if not(self.paused):
            win.blit(self.pause_img, (self.x, self.y))
        else:
            win.blit(self.play_img, (self.x, self.y))

class VerticalMenu(Menu):
    def __init__(self, x, y, bg):
        super().__init__([], x, y, bg, None)

    def draw(self, win):
        win.blit(self.bg, (self.x, self.y))
        for button in self.buttons:
            button.draw(win)
            text = self.font.render(str(button.value), 1, (255, 255, 255))
            win.blit(text, (button.x + 8, button.y + 65))
            win.blit(star_img, (button.x + 40, button.y + 62))


    def add_button(self, real_img, restricted_img, img, name, value):
        button_x = self.x + 15
        button_y = self.y + 35 + self.items*90
        button = VerticalButton(button_x, button_y, real_img, restricted_img, img, name, value)
        self.buttons.append(button)
        self.items += 1

    def clicked(self, x, y):
        for button in self.buttons:
            if button.click(x, y):
                return button
