import pygame

class Tower:

    def __init__(self):
        self.x = 50
        self.y = 50
        self.imgs = []
        self.img = None
        self.animation_count = 0

    def draw(self, win):
        self.img = self.imgs[self.animation_count//4]

        self.animation_count += 1

        if self.animation_count >= len(self.imgs)*4:
            self.animation_count = 0

        win.blit(self.img, (self.x, self.y))