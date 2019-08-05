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
from .towers.spear_tower import SpearTower
from .towers.archer_tower import ArcherTower
from .towers.village_tower import VillageTower
from .towers.support_towers import RangeTower
from .menu.menu import VerticalMenu, PlayPauseButton
from random import randrange
from .enemies.enemy import Enemy

spear_tower_icon = pygame.transform.scale(pygame.image.load(os.path.join("tower_defense\imgs\icons", "tw1_icon.png")),(50, 60))
archer_tower_icon = pygame.transform.scale(pygame.image.load(os.path.join("tower_defense\imgs\icons", "tw2_icon.png")),(50, 60))
village_tower_icon = pygame.transform.scale(pygame.image.load(os.path.join("tower_defense\imgs\icons", "tw3_icon.png")),(50, 60))
support_tower_icon = pygame.transform.scale(pygame.image.load(os.path.join("tower_defense\imgs\icons", "tw4_icon.png")),(50, 60))
spear_tower_img = pygame.transform.scale(pygame.image.load(os.path.join("tower_defense\imgs\\towers\\tower1_level1", "t1.png")),(78, 156))
archer_tower_img = pygame.transform.scale(pygame.image.load(os.path.join("tower_defense\imgs\\towers\\tower2_level1", "1.png")),(120, 141))
village_tower_img = pygame.transform.scale(pygame.image.load(os.path.join("tower_defense\imgs\\towers\\tower3_level1", "1.png")),(120, 141))
support_tower_img = pygame.transform.scale(pygame.image.load(os.path.join("tower_defense\imgs\\towers\\support_towers", "tower1_level1_damage.png")),(80, 80))
restricted_spear_tower_img = pygame.transform.scale(pygame.image.load(os.path.join("tower_defense\imgs\\towers\\tower1_level1", "restricted_t1.png")),(78, 156))
restricted_archer_tower_img = pygame.transform.scale(pygame.image.load(os.path.join("tower_defense\imgs\\towers\\tower2_level1", "restricted_1.png")),(120, 141))
restricted_village_tower_img = pygame.transform.scale(pygame.image.load(os.path.join("tower_defense\imgs\\towers\\tower3_level1", "restricted_1.png")),(120, 141))
restricted_support_tower_img = pygame.transform.scale(pygame.image.load(os.path.join("tower_defense\imgs\\towers\\support_towers", "restricted_tower1_level1_damage.png")),(80, 80))
play_button = pygame.transform.scale(pygame.image.load(os.path.join("tower_defense\imgs\icons", "play.png")), (70, 60))
pause_button = pygame.transform.scale(pygame.image.load(os.path.join("tower_defense\imgs\icons", "pause.png")), (70, 60))

pygame.init()

pygame.mixer.music.load(os.path.join("tower_defense\sounds", "bg_music.mp3"))

class TowerDefenseGame:

    def __init__(self):
        self.width = 1000
        self.height = 600
        self.win = pygame.display.set_mode((self.width, self.height))
        self.enemies = []
        self.towers = [VillageTower(500, 300)]
        self.support_towers = [RangeTower(140, 380)]
        self.lives = 8
        self.budget = 5000
        self.menu_bg = pygame.transform.rotate(
                        pygame.transform.scale(pygame.image.load(os.path.join("tower_defense\imgs\menu", "bg.png")), (450, 100)), 90)
        self.menu = VerticalMenu(self.width - 100, 100, self.menu_bg)
        self.menu.add_button(village_tower_img, restricted_village_tower_img, village_tower_icon, "village_tower_button", 500)
        self.menu.add_button(archer_tower_img, restricted_archer_tower_img, archer_tower_icon, "archer_tower_button", 800)
        self.menu.add_button(spear_tower_img, restricted_spear_tower_img, spear_tower_icon, "spear_tower_button", 1000)
        self.menu.add_button(support_tower_img, restricted_support_tower_img, support_tower_icon, "support_tower_button", 500)
        self.bg_img = pygame.image.load(os.path.join("tower_defense\imgs\maps", "Game_Map_1.jpg"))
        self.heart_img = None
        self.heart_imgs = []
        self.heart_animation_count = 0
        self.star_img = None
        self.star_imgs = []
        self.star_animation_count = 0
        self.side_button = None
        self.side_button_clicked = False
        self.button_name = ""
        self.button_value = 0
        self.pos = [0,0]
        for x in range(1,30):
            self.heart_imgs.append(
                pygame.transform.scale(pygame.image.load(os.path.join("tower_defense\imgs\icons\heart", "Layer " + str(x) + ".png")), (32, 32)))
        for x in range(1,9):
            self.star_imgs.append(
                pygame.transform.scale(pygame.image.load(os.path.join("tower_defense\imgs\icons\star", str(x) + ".png")), (32, 32)))
        self.clicks = [] # to be removed
        self.timer = time.time()
        self.font = pygame.font.SysFont("comicsans", 45)
        self.selected_tower = None

        self.wave = [
                        [18, 0, 18, 0, 0],
                        [0, 18, 0, 18, 0],
                        [18, 0, 18, 0, 18],
                        [18, 0, 18 , 0, 18],
                        [18, 18, 0 , 18, 0],
                        [0, 18, 18 , 18, 0],
                        [0, 18, 0 , 18, 18],
                        [18, 18, 18 , 18, 18],
                    ]
        self.wave_turn = 0
        self.enemy_type = [Archer_1(), Archer_2(), Archer_3(), Ninja(), Knight()]

        self.pause_button = PlayPauseButton(10, self.height - 70, play_button, play_button, pause_button)
        self.paused = False

        self.drawable = True

    def run(self):

        pygame.mixer.music.play(1)

        run = True

        clock = pygame.time.Clock()

        while run:
            if time.time() - self.timer >= random.randrange(1,5):
                self.timer = time.time()
                if not (self.paused):
                    if self.wave_turn < len(self.wave):
                        if (self.wave[self.wave_turn][0], self.wave[self.wave_turn][1], self.wave[self.wave_turn][2],
                            self.wave[self.wave_turn][3], self.wave[self.wave_turn][4]) == (0,0,0,0,0):
                            self.wave_turn += 1
                        enemy_index = randrange(5)
                        if self.wave[self.wave_turn][enemy_index] > 0:
                            self.wave[self.wave_turn][enemy_index] -= 1
                            # self.enemies.append(self.enemy_type[enemy_index])
                            # print(self.wave)
                            if enemy_index == 0:
                                self.enemies.append(Archer_1())
                            elif enemy_index == 1:
                                self.enemies.append(Archer_2())
                            elif enemy_index == 2:
                                self.enemies.append(Archer_3())
                            elif enemy_index == 3:
                                self.enemies.append(Ninja())
                            elif enemy_index == 4:
                                self.enemies.append(Knight())
                            # print(self.wave)
                            #print("wave turn " + str(self.wave_turn) + " enemy type " + str(self.enemy_type[enemy_index].id))
                    #self.enemies.append(random.choice([Archer_1(), Archer_2(), Archer_3(), Ninja(), Knight()]))
                    #self.enemies.append(Archer_1())
            clock.tick(150)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                self.pos = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # self.clicks.append(pos)
                    # print(self.clicks)
                    if self.pause_button.click(self.pos[0], self.pos[1]):
                        if not (self.paused):
                            self.pause_button.paused = True
                            self.paused = True
                        else:
                            self.pause_button.paused = False
                            self.paused = False

                    button_clicked = None
                    if self.selected_tower:
                        button_clicked = self.selected_tower.menu.clicked(self.pos[0], self.pos[1])
                        if button_clicked:
                            if button_clicked == "Upgrade":
                                #self.selected_tower.upgrade()
                                cost = self.selected_tower.menu.item_cost[self.selected_tower.level-1]
                                if cost <= self.budget:
                                    self.budget -= cost
                                    self.selected_tower.upgrade()
                                else:
                                    print("Budget is not enough")
                            if button_clicked == "Sell":
                                self.budget += self.selected_tower.value[self.selected_tower.level - 1]
                                if self.towers.count(self.selected_tower) > 0:
                                    self.towers.remove(self.selected_tower)
                                else:
                                    self.support_towers.remove(self.selected_tower)
                    if not(button_clicked):
                        for t in self.towers:
                            if t.click(self.pos[0], self.pos[1]):
                                t.selected = True
                                self.selected_tower = t
                            else:
                                t.selected = False
                        for t in self.support_towers:
                            if t.click(self.pos[0], self.pos[1]):
                                t.selected = True
                                self.selected_tower = t
                            else:
                                t.selected = False

                    if self.side_button is None:
                        self.side_button = self.menu.clicked(self.pos[0], self.pos[1])


                    if self.side_button_clicked:
                        self.side_button_clicked = False
                        if self.drawable:
                            if self.button_name == "village_tower_button" and self.budget >= self.button_value:
                                self.towers.append(VillageTower(self.pos[0] - 60, self.pos[1] - 70))
                                self.budget -= self.button_value
                            elif self.button_name == "archer_tower_button" and self.budget >= self.button_value:
                                self.towers.append(ArcherTower(self.pos[0] - 60, self.pos[1] - 70))
                                self.budget -= self.button_value
                            elif self.button_name == "spear_tower_button" and self.budget >= self.button_value:
                                self.towers.append(SpearTower(self.pos[0] - 39, self.pos[1] - 78))
                                self.budget -= self.button_value
                            elif self.button_name == "support_tower_button" and self.budget >= self.button_value:
                                self.support_towers.append(RangeTower(self.pos[0] - 40, self.pos[1] - 40))
                                self.budget -= self.button_value
                            self.side_button = None

                    if self.side_button and not(self.side_button_clicked):
                        self.side_button_clicked = True
                        self.button_name = self.side_button.name
                        self.button_value = self.side_button.value




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
            if not(self.paused):
                for t in self.towers:
                    self.budget += t.attack(self.enemies)

            for st in self.support_towers:
                st.increase_range(self.towers)


            self.draw(self.paused)

        pygame.quit()

    def draw(self, paused):
        self.win.blit(self.bg_img, (0,0))
        # for c in path:
          #  pygame.draw.circle(self.win, (255, 0, 0), (c[0], c[1]), 5, 0)
        for enemy in self.enemies:
            enemy.draw(self.win, paused)
        for tower in self.towers:
            tower.draw(self.win, paused)
        for st in self.support_towers:
            st.draw(self.win)
        text = self.font.render(str(self.lives), 1, (255,255,255))
        self.win.blit(text, (self.width-90, 10))
        text2 = self.font.render(str(self.budget), 1, (255, 255, 255))
        self.win.blit(text2, (self.width - 140, 50))
        self.draw_heart()
        self.draw_star()

        if self.selected_tower:
            self.selected_tower.draw(self.win, paused)

        self.menu.draw(self.win)

        self.pause_button.draw(self.win)

        if self.side_button_clicked and self.side_button:
            self.drawable = self.side_button.draw_moving_button(self.win, self.pos[0], self.pos[1], self.towers, Enemy().path1)


        pygame.init()
        pygame.display.update()

    def draw_heart(self):
        self.heart_img = self.heart_imgs[self.heart_animation_count // 4]
        self.heart_animation_count += 1

        if self.heart_animation_count >= len(self.heart_imgs) * 4:
            self.heart_animation_count = 0

        self.win.blit(self.heart_img, (self.width-60, 5))

    def draw_star(self):
        self.star_img = self.star_imgs[self.star_animation_count // 4]
        self.star_animation_count += 1

        if self.star_animation_count >= len(self.star_imgs) * 4:
            self.star_animation_count = 0

        self.win.blit(self.star_img, (self.width-60, 50))