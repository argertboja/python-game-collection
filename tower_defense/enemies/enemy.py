import pygame
import math

class Enemy:
    # Class Variables


    def __init__(self):
        self.width = 148
        self.height = 148
        self.animation_count = 0
        self.health = 1
        self.path1 = [(1, 375), (40, 369), (72, 355), (109, 335), (147, 302), (178, 279), (222, 266), (257, 265), (289, 267), (325, 283), (355, 310), (389, 343), (414, 371), (444, 400), (483, 425), (513, 435), (545, 446), (574, 457), (617, 456), (660, 455), (704, 450), (737, 451), (761, 427), (791, 409), (813, 381), (826, 337), (838, 294), (843, 264), (814, 243), (784, 222), (770, 188), (762, 128), (749, 86), (725, 51), (709, 6), (-28,6)]
        self.path2 = [(1, 373), (29, 370), (63, 358), (97, 343), (124, 321), (159, 291), (202, 271), (249, 265), (290, 263), (331, 284), (358, 316), (390, 346), (421, 372), (448, 401), (487, 424), (525, 439), (566, 448), (571, 473), (548, 497), (525, 514), (502, 533), (483, 561), (467, 588), (480, 613), (498, 635), (519, 653), (541, 682), (554, 696)]
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

    def draw(self, win):
        """
         Draw enemy based on images
         :param win: surface
         :return: none
        """

        self.img = self.imgs[self.animation_count//4]
        self.animation_count += 1

        if self.animation_count >= len(self.imgs)*4:
            self.animation_count = 0

        win.blit(self.img, (self.x, self.y))

        self.move()


    def collide(self, x, y):
        """
        Return if object collides the enemy
        :param x: int
        :param y: int
        :return: bool
        """
        if x >= self.x and x <= (self.x + self.width):
            if y >= self.y and y <= (self.y + self.height):
                return True
        return False

    def move(self):
        """
        Move enemy
        :return: none
        """
        """if self.path_round == 0:
            path = self.path1
            self.path_round = 1
        else:
            path = self.path2
            self.path_round = 0
        print(path)"""
        path = self.path1


        x1, y1 = path[self.path_pos]

        if self.path_pos + 1 >= len(path):
            self.x2, y2 = (-20, 6)
        else:
            self.x2, y2 = path[self.path_pos + 1]

        direction_vector = ((self.x2-x1), (y2-y1))
        length = math.sqrt((direction_vector[0])**2 + (direction_vector[1])**2)
        direction_vector = (direction_vector[0]/length, direction_vector[1]/length)

        if direction_vector[0] < 0 and not(self.flipped):
            self.flipped = True
            for x, img in enumerate(self.imgs):
                self.imgs[x] = pygame.transform.flip(img, True, False)

        move_x, move_y = (self.x + direction_vector[0], self.y + direction_vector[1])

        self.x = move_x
        self.y = move_y
        print(self.x)

        if direction_vector[0] >= 0:
            if direction_vector[1] >= 0:
                if self.x >= self.x2 and self.y >= y2:
                    self.path_pos += 1
            else:
                if self.x >= self.x2 and self.y <= y2:
                    self.path_pos += 1
        else:
            if direction_vector[1] >= 0:
                if self.x <= self.x2 and self.y >= y2:
                    self.path_pos += 1
            else:
                if self.x <= self.x2 and self.y <= y2:
                    self.path_pos += 1

    def hit(self):
        """
        Remove enemy health by 1 and return true if enemy is dead
        :return: bool
        """
        self.health -= 1
        if self.health <= 0:
            return True