import os

import pygame


class TowerDefenseGame:

    def __init__(self):
        self.width = 1000
        self.height = 700
        self.win = pygame.display.set_mode((self.width, self.height))
        self.enemies = []
        self.towers = []
        self.lives = 8
        self.budget = 800
        self.bg_img = pygame.image.load(os.path.join("imgs", "Game_Map_1.jpg"))

    def run(self):
        run = True

        clock = pygame.time.Clock()

        while run:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                self.draw()

        pygame.quit()

    def draw(self):
        self.win.blit(self.bg_img, (0,0))
        pygame.display.update()