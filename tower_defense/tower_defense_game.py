import os

import pygame
from .enemies.knight import Knight
from .enemies.ninja import Ninja
from .enemies.archer_1 import Archer_1
from .enemies.archer_2 import Archer_2
from .enemies.archer_3 import Archer_3
from .towers.chinese_tower import ChineseTower


class TowerDefenseGame:

    def __init__(self):
        self.width = 1000
        self.height = 700
        self.win = pygame.display.set_mode((self.width, self.height))
        self.enemies = [Knight(), Ninja(), Archer_1(), Archer_2(), Archer_3()]
        self.towers = [ChineseTower()]
        self.lives = 8
        self.budget = 800
        self.bg_img = pygame.image.load(os.path.join("tower_defense\imgs\maps", "Game_Map_1.jpg"))
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
            to_del = []

            for enemy in self.enemies:
                if enemy.x2 < -8:
                    to_del.append(enemy)

            for d in to_del:
                self.enemies.remove(d)
            self.draw()

        pygame.quit()

    def draw(self):
        self.win.blit(self.bg_img, (0,0))
        # for c in path:
          #  pygame.draw.circle(self.win, (255, 0, 0), (c[0], c[1]), 5, 0)
        for enemy in self.enemies:
            enemy.draw(self.win)
        for tower in self.towers:
            tower.draw(self.win)
        pygame.init()
        pygame.display.update()