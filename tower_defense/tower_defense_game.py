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
        self.bg_img = pygame.image.load(os.path.join("tower_defense\imgs", "Game_Map_1.jpg"))
        self.clicks = [] # to be removed

    def run(self):
        run = True

        clock = pygame.time.Clock()

        while run:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                # pos = pygame.mouse.get_pos()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # self.clicks.append(pos)
                    # print(self.clicks)
                    pass

            self.draw()

        pygame.quit()

    def draw(self):
        self.win.blit(self.bg_img, (0,0))
        # for c in self.clicks:
           # pygame.draw.circle(self.win, (255,0,0), (c[0], c[1]), 5, 0)
        pygame.display.update()