import os
import time
import random

import pygame
pygame.font.init()
from .enemies.knight import Knight
from .enemies.ninja import Ninja
from .enemies.archer_1 import Archer_1
from .enemies.archer_2 import Archer_2
from .enemies.archer_3 import Archer_3
from .towers.chinese_tower import ChineseTower
from .towers.spear_tower import SpearTower
from .towers.archer_tower import ArcherTower
from .towers.village_tower import VillageTower
from .towers.support_towers import RangeTower


class TowerDefenseGame:

    def __init__(self):
        self.width = 1000
        self.height = 600
        self.win = pygame.display.set_mode((self.width, self.height))
        self.enemies = []
        self.towers = [SpearTower(80, 300), SpearTower(250, 300), ArcherTower(300, 300), VillageTower(500, 300)]
        self.support_towers = [RangeTower(140, 380)]
        self.lives = 8
        self.budget = 800
        self.bg_img = pygame.image.load(os.path.join("tower_defense\imgs\maps", "Game_Map_1.jpg"))
        self.heart_img = None
        self.heart_imgs = []
        self.heart_animation_count = 0
        for x in range(1,30):
            self.heart_imgs.append(
                pygame.image.load(os.path.join("tower_defense\imgs\icons\heart", "Layer " + str(x) + ".png")))
        self.clicks = [] # to be removed
        self.timer = time.time()
        self.font = pygame.font.SysFont("comicsans", 60)
        self.selected_tower = None

    def run(self):
        run = True

        clock = pygame.time.Clock()

        while run:
            if time.time() - self.timer >= random.randrange(1,5):
                self.timer = time.time()
                self.enemies.append(random.choice([Archer_1(), Archer_2(), Archer_3(), Ninja(), Knight()]))
                #self.enemies.append(Archer_1())
            clock.tick(120)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                pos = pygame.mouse.get_pos()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # self.clicks.append(pos)
                    # print(self.clicks)
                    for t in self.towers:
                        if t.click(pos[0], pos[1]):
                            t.selected = True
                            self.selected_tower = t
                        else:
                            t.selected = False
                    for t in self.support_towers:
                        if t.click(pos[0], pos[1]):
                            t.selected = True
                            self.selected_tower = t
                        else:
                            t.selected = False
            to_del = []

            for enemy in self.enemies:
                if enemy.x2 < -8:
                    to_del.append(enemy)

            for d in to_del:
                self.enemies.remove(d)
                self.lives -= 1
                if self.lives <= 0:
                    print("You lost!")
                    run = False

            for t in self.towers:
                t.attack(self.enemies)

            for st in self.support_towers:
                st.increase_range(self.towers)


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
        for st in self.support_towers:
            st.draw(self.win)
        text = self.font.render(str(self.lives), 1, (255,255,255))
        self.win.blit(text, (self.width-90, 10))
        self.draw_heart()
        pygame.init()
        pygame.display.update()

    def draw_heart(self):
        self.heart_img = self.heart_imgs[self.heart_animation_count // 4]
        self.heart_animation_count += 1

        if self.heart_animation_count >= len(self.heart_imgs) * 4:
            self.heart_animation_count = 0

        self.win.blit(self.heart_img, (self.width-60, 5))