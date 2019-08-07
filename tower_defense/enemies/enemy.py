"""
@author: Argert Boja
@org: ABEnt
@date: May 2019
@description: The enemy class which has the main functionality of the enemies
"""

# import packages
import pygame
import math


class Enemy:
    def __init__(self):
        self.width = 148
        self.height = 148
        self.animation_count = 0
        self.health = 0
        self.max_health = 0
        self.path1 = [(-8, 375),(1, 375), (40, 369), (72, 355), (109, 335), (147, 302), (178, 279), (222, 266), (257, 265), (289, 267), (325, 283), (355, 310), (389, 343), (414, 371), (444, 400), (483, 425), (513, 435), (545, 446), (574, 457), (617, 456), (660, 455), (704, 450), (737, 451), (761, 427), (791, 409), (813, 381), (826, 337), (838, 294), (843, 264), (814, 243), (784, 222), (770, 188), (762, 128), (749, 86), (725, 51), (709, 6), (-28, 6)]
        self.x = self.path1[0][0]
        self.y = self.path1[0][1]
        self.x2 = 20
        self.path_round = 0
        self.img = None
        self.velocity = 4
        self.path_pos = 0
        self.move_count = 0
        self.imgs = []
        self.flipped = False
        self.id = 1
        self.direction_vector = (0,0)

    def draw(self, win, paused):
        """
         Draw enemy based on images
         :param win: surface
         :return: none
        """

        self.img = self.imgs[self.animation_count//5]
        if not(paused):
            self.animation_count += 1

        if self.animation_count >= len(self.imgs)*5:
            self.animation_count = 0

        win.blit(self.img, (self.x - self.img.get_width()/2 - 10, self.y - (self.img.get_height()/2+15)))
        self.draw_health_bar(win)
        if not(paused):
            self.move()

    def draw_health_bar(self, win):
        """
        Draw health bar for each enemy
        :param win:
        :return:
        """
        health_bar_length = 50
        move_by = round(health_bar_length / self.max_health)
        health_bar = move_by * self.health

        pygame.draw.rect(win, (255, 0, 0), (self.x - 35, self.y - 58, health_bar_length,10) , 0)
        pygame.draw.rect(win, (0, 255, 0), (self.x - 35, self.y - 58, health_bar, 10), 0)

    def move(self):
        """
        Move enemy
        :return: none
        """
        path = self.path1

        self.x1, self.y1 = path[self.path_pos]

        if self.path_pos + 1 >= len(path):
            self.x2, self.y2 = (-28, 6)
        else:
            self.x2, self.y2 = path[self.path_pos + 1]

        self.direction_vector = ((self.x2-self.x1)*2, (self.y2-self.y1)*2)
        length = math.sqrt((self.direction_vector[0])**2 + (self.direction_vector[1])**2)
        self.direction_vector = (self.direction_vector[0]/length, self.direction_vector[1]/length)

        # flip images in case of turning direction
        if self.direction_vector[0] < 0 and not(self.flipped):
            self.flipped = True
            for x, img in enumerate(self.imgs):
                self.imgs[x] = pygame.transform.flip(img, True, False)

        move_x, move_y = (self.x + self.direction_vector[0], self.y + self.direction_vector[1])

        self.x = move_x
        self.y = move_y

        if self.direction_vector[0] >= 0:
            if self.direction_vector[1] >= 0:
                if self.x >= self.x2 and self.y >= self.y2:
                    self.path_pos += 1
            else:
                if self.x >= self.x2 and self.y <= self.y2:
                    self.path_pos += 1
        else:
            if self.direction_vector[1] >= 0:
                if self.x <= self.x2 and self.y >= self.y2:
                    self.path_pos += 1
            else:
                if self.x <= self.x2 and self.y <= self.y2:
                    self.path_pos += 1

    def hit(self, damage):
        """
        Remove enemy health by 1 and return true if enemy is dead
        :return: bool
        """
        self.health -= damage
        if self.health <= 0:
            return True
        return False