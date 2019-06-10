class Enemy:
    # Class Variables
    imgs = []

    def __init__(self, x_pos, y_pos, width, height):
        self.x = x_pos
        self.y = y_pos
        self.width = width
        self.height = height
        self.animation_count = 0
        self.health = 1
        self.path1 = [(1, 375), (40, 369), (72, 355), (109, 335), (147, 302), (178, 279), (222, 266), (257, 265), (289, 267), (325, 283), (355, 310), (389, 343), (414, 371), (444, 400), (483, 425), (513, 435), (545, 446), (574, 457), (617, 456), (660, 455), (704, 450), (737, 451), (761, 427), (791, 409), (791, 409), (813, 381), (826, 337), (838, 294), (843, 264), (814, 243), (784, 222), (770, 188), (762, 128), (749, 86), (725, 51), (709, 6)]
        self.path2 = [(1, 373), (29, 370), (63, 358), (97, 343), (124, 321), (159, 291), (202, 271), (249, 265), (290, 263), (331, 284), (358, 316), (390, 346), (421, 372), (448, 401), (487, 424), (525, 439), (566, 448), (571, 473), (548, 497), (525, 514), (502, 533), (483, 561), (467, 588), (480, 613), (498, 635), (519, 653), (541, 682), (554, 696)]
        self.img = None
        self.velocity = 3

    def draw(self, win):
        self.animation_count += 1
        self.img = self.imgs[self.animation_count]

        if self.animation_count >= len(self.imgs):
            self.animation_count = 0

        win.blit(self.img, (self.x, self.y))

        self.move()
        """
        Draw enemy based on images
        :param win: surface
        :return: none
        """

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
        pass

    def hit(self):
        """
        Remove enemy health by 1 and return true if enemy is dead
        :return: bool
        """
        self.health -= 1
        if self.health <= 0:
            return True