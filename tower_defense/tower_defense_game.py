"""
@author: Argert Boja
@org: ABEnt
@date: May 2019
@description: This is a clone of Tower Defense Game which I implemented in Python
"""

# import packages
import os
import time
import random
import pygame
from random import randrange

# import classes
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

# load images
# tower icons on menu
spear_tower_icon = pygame.transform.scale(pygame.image.load(os.path.join("tower_defense\imgs\icons", "tw1_icon.png")),(50, 60))
archer_tower_icon = pygame.transform.scale(pygame.image.load(os.path.join("tower_defense\imgs\icons", "tw2_icon.png")),(50, 60))
village_tower_icon = pygame.transform.scale(pygame.image.load(os.path.join("tower_defense\imgs\icons", "tw3_icon.png")),(50, 60))
support_tower_icon = pygame.transform.scale(pygame.image.load(os.path.join("tower_defense\imgs\icons", "tw4_icon.png")),(50, 60))
you_lost_menu = pygame.transform.scale(pygame.image.load(os.path.join("tower_defense\imgs\menu", "you_lost.png")),(500, 300))
you_won_menu = pygame.transform.scale(pygame.image.load(os.path.join("tower_defense\imgs\menu", "you_won.png")),(500, 300))
start_game_menu = pygame.transform.scale(pygame.image.load(os.path.join("tower_defense\imgs\menu", "start_game.png")),(500, 366))
start_game_menu_yes = pygame.transform.scale(pygame.image.load(os.path.join("tower_defense\imgs\menu", "start_game_yes.png")),(500, 366))
start_game_menu_no = pygame.transform.scale(pygame.image.load(os.path.join("tower_defense\imgs\menu", "start_game_no.png")),(500, 366))
yes_button = pygame.transform.scale(pygame.image.load(os.path.join("tower_defense\imgs\menu", "yes_button.png")),(138, 63))
no_button = pygame.transform.scale(pygame.image.load(os.path.join("tower_defense\imgs\menu", "no.png")),(138, 63))

# tower images while dragging
spear_tower_img = pygame.transform.scale(pygame.image.load(os.path.join("tower_defense\imgs\\towers\\tower1_level1", "t1.png")),(78, 156))
archer_tower_img = pygame.transform.scale(pygame.image.load(os.path.join("tower_defense\imgs\\towers\\tower2_level1", "1.png")),(120, 141))
village_tower_img = pygame.transform.scale(pygame.image.load(os.path.join("tower_defense\imgs\\towers\\tower3_level1", "1.png")),(120, 141))
support_tower_img = pygame.transform.scale(pygame.image.load(os.path.join("tower_defense\imgs\\towers\\support_towers", "tower1_level1_damage.png")),(80, 80))

# tower images while dragging in restricted areas
restricted_spear_tower_img = pygame.transform.scale(pygame.image.load(os.path.join("tower_defense\imgs\\towers\\tower1_level1", "restricted_t1.png")),(78, 156))
restricted_archer_tower_img = pygame.transform.scale(pygame.image.load(os.path.join("tower_defense\imgs\\towers\\tower2_level1", "restricted_1.png")),(120, 141))
restricted_village_tower_img = pygame.transform.scale(pygame.image.load(os.path.join("tower_defense\imgs\\towers\\tower3_level1", "restricted_1.png")),(120, 141))
restricted_support_tower_img = pygame.transform.scale(pygame.image.load(os.path.join("tower_defense\imgs\\towers\\support_towers", "restricted_tower1_level1_damage.png")),(80, 80))

# button images
play_button = pygame.transform.scale(pygame.image.load(os.path.join("tower_defense\imgs\icons", "play.png")), (70, 60))
pause_button = pygame.transform.scale(pygame.image.load(os.path.join("tower_defense\imgs\icons", "pause.png")), (70, 60))
play_music_button = pygame.transform.scale(pygame.image.load(os.path.join("tower_defense\imgs\icons", "play_music.png")), (110, 50))
mute_music_button = pygame.transform.scale(pygame.image.load(os.path.join("tower_defense\imgs\icons", "mute_music.png")), (110, 50))

# icons and backgrounds
icon = pygame.transform.scale(pygame.image.load(os.path.join("images", "icon.png")),(32,32))
menu_bg = pygame.transform.scale(pygame.image.load(os.path.join("tower_defense\imgs\menu", "vertical_menu_bg.png")), (85, 410))
bg_img = pygame.image.load(os.path.join("tower_defense\imgs\maps", "Game_Map_1.jpg"))

# initialize pygame
pygame.init()
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100, 100)
pygame.display.set_icon(icon)
pygame.display.set_caption("Tower Defense")

# load music and sounds
pygame.mixer.music.load(os.path.join("tower_defense\sounds", "bg_music.mp3"))
pygame.mixer.music.set_volume(0.5)
button_sound = pygame.mixer.Sound(os.path.join("tower_defense\sounds", "button-16.wav"))
coins_sound = pygame.mixer.Sound(os.path.join("tower_defense\sounds", "button-16.wav"))

# Button class for adding new buttons in the main menu
class Button:
    # initialization for button
    def __init__(self, x, y, img, hover_img, name):
        """
        Button initialization method
        :param x: x position of button
        :param y: y position of button
        :param img: main image
        :param hover_img: hover image
        """
        self.x = x
        self.y = y
        self.img = img
        self.original_img = img
        self.hover_img = hover_img
        self.width = self.height = 0
        if self.img is not None:
            self.width = self.img.get_width()
            self.height = self.img.get_height()
        self.name = name

    def click(self, x, y):
        """
        This method returns true if button is clicked
        :param x: mouse x position
        :param y: mouse y position
        :return: bool
        """
        if self.x <= x <= self.x + self.width:
            if self.y <= y <= self.y + self.height:
                return True

        return False

    def mouse_hover(self, x, y):
        """
        This method changes the image of button on mouse hover
        :param x:
        :param y:
        :return:
        """
        if self.click(x, y):
            self.img = self.hover_img
        else:
            self.img = self.original_img


    def draw(self, win):
        """
        This method draws button
        :param win: surface
        :return: none
        """
        win.blit(self.img, (self.x, self.y))

class TowerDefenseGame:

    def __init__(self):
        self.width = 1000
        self.height = 600
        self.win = pygame.display.set_mode((self.width, self.height))
        self.enemies = []
        self.enemy_type = [Archer_1(), Archer_2(), Archer_3(), Ninja(), Knight()]
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
        self.towers = []
        self.support_towers = []
        self.lives = 8
        self.budget = 1000
        self.menu_bg = menu_bg

        # initialize side menu and buttons
        self.menu = VerticalMenu(self.width - 90, 120, self.menu_bg)
        self.menu.add_button(village_tower_img, restricted_village_tower_img, village_tower_icon, "village_tower_button", 500)
        self.menu.add_button(archer_tower_img, restricted_archer_tower_img, archer_tower_icon, "archer_tower_button", 800)
        self.menu.add_button(spear_tower_img, restricted_spear_tower_img, spear_tower_icon, "spear_tower_button", 1000)
        self.menu.add_button(support_tower_img, restricted_support_tower_img, support_tower_icon, "support_tower_button", 500)
        self.side_button = None
        self.side_button_clicked = False
        self.button_name = ""
        self.button_value = 0

        # start game buttons
        self.yes_button = None
        self.no_button = None

        # map image
        self.bg_img = bg_img

        # heart animation
        self.heart_img = None
        self.heart_imgs = []
        self.heart_animation_count = 0
        for x in range(1,30):
            self.heart_imgs.append(
                pygame.transform.scale(pygame.image.load(os.path.join("tower_defense\imgs\icons\heart", "Layer " + str(x) + ".png")), (32, 32)))

        # star animation
        self.star_img = None
        self.star_imgs = []
        self.star_animation_count = 0
        for x in range(1,9):
            self.star_imgs.append(
                pygame.transform.scale(pygame.image.load(os.path.join("tower_defense\imgs\icons\star", str(x) + ".png")), (32, 32)))


        self.pos = [0,0]

        # self.clicks = [] # used for adding restricted areas

        # initialize timer
        self.timer = time.time()

        # create font
        self.font = pygame.font.SysFont("comicsans", 45)

        # selected tower
        self.selected_tower = None

        # low buttons
        self.pause_button = PlayPauseButton(10, self.height - 70, pause_button, play_button, pause_button)
        self.mute_music_button = PlayPauseButton(85, self.height - 60, play_music_button, mute_music_button, play_music_button)

        # pause game toggle
        self.paused = True

        # drawable toggle for new tower
        self.drawable = True

        # sound toggles
        self.mute_sounds = False
        self.mute_music = False

        # start game toggle
        self.start = True
        self.restart = False

        # restricted areas
        self.restricted = [ (23, 89), (74, 95), (111, 96), (161, 93), (202, 77), (233, 77), (266, 81), (291, 114), (328, 106),
                           (374, 84), (409, 57), (433, 18), (388, 13), (332, 12), (287, 12), (233, 12), (183, 11), (140, 12), (82, 10),
                           (16, 13), (18, 48), (68, 45), (117, 43), (145, 43), (185, 43), (228, 43), (263, 46), (311, 49), (359, 46),
                           (394, 37), (539, 132), (527, 169), (531, 218), (548, 255), (568, 285), (607, 293), (634, 272), (634, 235), (617, 197),
                           (601, 177), (567, 152), (573, 192), (582, 255), (609, 254), (586, 223), (533, 84), (522, 53), (541, 37), (558, 62),
                           (166, 590), (211, 560), (240, 535), (271, 504), (312, 460), (262, 459), (227, 461), (200, 482), (168, 512), (158, 536),
                           (208, 523), (239, 492), (884, 174), (860, 164), (845, 121), (850, 80), (885, 55), (911, 36), (934, 47), (953, 83),
                           (961, 108), (912, 90), (889, 112), (903, 176), (878, 140), (827, 106), (858, 62), (25, 373), (54, 370), (85, 352),
                           (114, 330), (143, 306), (182, 285), (217, 267), (249, 264), (287, 263), (321, 277), (343, 294), (370, 319), (391, 346),
                           (410, 364), (430, 386), (456, 408), (479, 426), (506, 442), (526, 451), (23, 371), (67, 363), (97, 342), (97, 342),
                            (135, 313), (174, 284), (214, 269), (262, 261), (315, 262), (336, 289), (372, 325), (402, 358), (430, 384), (463, 415),
                            (495, 438), (530, 459), (571, 470), (622, 463), (672, 459), (720, 450), (764, 436), (788, 403), (814, 356), (831, 312),
                            (850, 265), (809, 233), (778, 187), (768, 145), (755, 94), (730, 48), (707, 12), (886, 252), (769, 484), (811, 506),
                            (848, 515), (887, 541), (925, 562), (962, 580), (544, 510), (525, 536), (507, 560), (465, 563), (410, 570), (371, 585),
                            (539, 584)]

    def run(self):
        # play music in case music is not mutted
        if not (self.mute_music):
            pygame.mixer.music.play(1)

        run = True

        clock = pygame.time.Clock()

        while run:
            # pause music in case mutted and play otherwise
            if(self.mute_music):
                pygame.mixer.music.pause()
            else:
                pygame.mixer.music.unpause()

            # generate enemies in different intervals
            if time.time() - self.timer >= random.randrange(1,4):
                self.timer = time.time()
                # if game is not paused play the game
                if not (self.paused):
                    if self.wave_turn < len(self.wave):
                        # increase wave turn if all enemies of a wave are generated
                        if (self.wave[self.wave_turn][0], self.wave[self.wave_turn][1], self.wave[self.wave_turn][2],
                            self.wave[self.wave_turn][3], self.wave[self.wave_turn][4]) == (0,0,0,0,0):
                            self.wave_turn += 1
                        # index for random enemy type
                        enemy_index = randrange(5)
                        # if there are enemies left to generate in a type do this
                        if self.wave[self.wave_turn][enemy_index] > 0:
                            self.wave[self.wave_turn][enemy_index] -= 1
                            # add new enemy depending on the index number
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
                    else:
                        self.win.blit(you_won_menu, (250, 150))
                        self.start = True
                        self.paused = True
                        self.reset_game()
            clock.tick(200)

            # get events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    self.start = False
                # get mouse position
                self.pos = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # self.clicks.append(self.pos) # used to add new point in restricted areas
                     # print(self.clicks)

                    # starting game buttons
                    if self.yes_button is not None and self.yes_button.click(self.pos[0], self.pos[1]):
                        self.start = False
                        self.paused = False
                        self.yes_button = None
                        self.no_button = None
                    elif self.no_button is not None and self.no_button.click(self.pos[0], self.pos[1]):
                        self.start = False
                        self.restart = False
                        run = False
                        self.yes_button = None
                        self.no_button = None

                    # pause button
                    if self.pause_button.click(self.pos[0], self.pos[1]):
                        button_sound.play(0)
                        if not (self.paused):
                            self.pause_button.paused = True
                            self.paused = True
                        else:
                            self.pause_button.paused = False
                            self.paused = False

                    # mute music button
                    if self.mute_music_button.click(self.pos[0], self.pos[1]):
                        if not (self.mute_music):
                            self.mute_music_button.paused = True
                            self.mute_music = True
                        else:
                            self.mute_music_button.paused = False
                            self.mute_music = False
                    # initialize button clicked
                    button_clicked = None

                    # check if one of the towers is selected
                    if self.selected_tower:
                        button_clicked = self.selected_tower.menu.clicked(self.pos[0], self.pos[1])
                        # check if one of the tower menu buttons is clicked
                        if button_clicked:
                            button_sound.play(0)
                            if button_clicked == "Upgrade":
                                cost = self.selected_tower.menu.item_cost[self.selected_tower.level-1]
                                # upgrade tower if budget permits
                                if cost <= self.budget:
                                    self.budget -= cost
                                    self.selected_tower.upgrade()
                                else:
                                    print("Budget is not enough")
                            # sell tower and increase budget according to tower value
                            if button_clicked == "Sell":
                                self.budget += self.selected_tower.value[self.selected_tower.level - 1]
                                if self.towers.count(self.selected_tower) > 0:
                                    self.towers.remove(self.selected_tower)
                                else:
                                    self.support_towers.remove(self.selected_tower)

                    # check if one of the towers is selected
                    if not(button_clicked):
                        for t in self.towers:
                            if t.click(self.pos[0], self.pos[1]):
                                button_sound.play(0)
                                t.selected = True
                                self.selected_tower = t
                            else:
                                t.selected = False
                        for t in self.support_towers:
                            button_sound.play(0)
                            if t.click(self.pos[0], self.pos[1]):
                                t.selected = True
                                self.selected_tower = t
                            else:
                                t.selected = False

                    # check if one of the side menu buttons is clicked
                    if self.side_button is None:
                        button_sound.play(0)
                        self.side_button = self.menu.clicked(self.pos[0], self.pos[1])

                    # if one of the buttons is clicked the tower is being dragged
                    if self.side_button_clicked:
                        self.side_button_clicked = False
                        # check if tower is not in a restricted area
                        if self.drawable:
                            button_sound.play(0)
                            # add new tower based on the tower type selected on the menu
                            if self.button_name == "village_tower_button" and self.budget >= self.button_value:
                                self.towers.append(VillageTower(self.pos[0] - 60, self.pos[1] - 70))
                                coins_sound.play()
                                self.budget -= self.button_value
                            elif self.button_name == "archer_tower_button" and self.budget >= self.button_value:
                                self.towers.append(ArcherTower(self.pos[0] - 60, self.pos[1] - 70))
                                coins_sound.play()
                                self.budget -= self.button_value
                            elif self.button_name == "spear_tower_button" and self.budget >= self.button_value:
                                self.towers.append(SpearTower(self.pos[0] - 39, self.pos[1] - 78))
                                coins_sound.play()
                                self.budget -= self.button_value
                            elif self.button_name == "support_tower_button" and self.budget >= self.button_value:
                                self.support_towers.append(RangeTower(self.pos[0] - 40, self.pos[1] - 40))
                                coins_sound.play()
                                self.budget -= self.button_value
                            self.side_button = None

                    # save button values
                    if self.side_button and not(self.side_button_clicked):
                        self.side_button_clicked = True
                        self.button_name = self.side_button.name
                        self.button_value = self.side_button.value

            # delete enemies that go off screen and reduce life number
            for enemy in self.enemies:
                if enemy.x2 < -8:
                    self.enemies.remove(enemy)
                    self.lives -= 1
                    if self.lives <= 0:
                        self.reset_game()

            # attack if game is not paused and enemies are in the range
            if not(self.paused):
                for t in self.towers:
                    # increase budget for every killed enemy
                    profit = t.attack(self.enemies)
                    self.budget += profit
                    if profit > 0:
                        coins_sound.play()

            # link support towers with attack towers
            for st in self.support_towers:
                st.increase_range(self.towers)

            # draw all images
            self.draw(self.paused, self.start, self.pos[0], self.pos[1])

        # quit game if lost
        self.win.blit(you_lost_menu, (250, 150))
        pygame.display.update()
        time.sleep(2)
        if not (self.restart):
            pygame.quit()

    def draw(self, paused, start, mouse_x, mouse_y):
        """
        Method for drawing all images and animations
        :param paused: boolean which checks whether game is paused or not
        :return: None
        """
        # draw background
        self.win.blit(self.bg_img, (0,0))

        # draw path or restricted areas points
        # for c in self.clicks:
          # pygame.draw.circle(self.win, (255, 0, 0), (c[0], c[1]), 5, 0)

        # draw enemies
        for enemy in self.enemies:
            enemy.draw(self.win, paused)

        # draw towers
        for tower in self.towers:
            tower.draw(self.win, paused)

        # draw support towers
        for st in self.support_towers:
            st.draw(self.win, paused)

        # draw texts for lives and budget
        text = self.font.render(str(self.lives), 1, (255,255,255))
        self.win.blit(text, (self.width-90, 10))
        text2 = self.font.render(str(self.budget), 1, (255, 255, 255))
        self.win.blit(text2, (self.width - 140, 50))

        # draw heart and star animations
        self.draw_heart()
        self.draw_star()

        # redraw selected tower
        if self.selected_tower:
            self.selected_tower.draw(self.win, paused)

        # draw menu and buttons
        self.menu.draw(self.win)
        self.pause_button.draw(self.win)
        self.mute_music_button.draw(self.win)

        # check if new tower is in restricted area
        if self.side_button_clicked and self.side_button:
            self.drawable = self.side_button.draw_moving_button(self.win, self.pos[0], self.pos[1], self.towers, self.support_towers, self.restricted)

        # draw initial menu
        if start:
            self.win.blit(start_game_menu, (250, 150))
            self.yes_button = Button(343, 435, yes_button, yes_button, "yes")
            self.no_button = Button(521, 435, no_button, no_button, "no")
            if self.yes_button.click(mouse_x, mouse_y):
                self.win.blit(start_game_menu_yes, (250, 150))
            if self.no_button.click(mouse_x, mouse_y):
                self.win.blit(start_game_menu_no, (250, 150))

        pygame.display.update()

    def draw_heart(self):
        """
        Method for drawing heart animation of lives
        :return: None
        """
        self.heart_img = self.heart_imgs[self.heart_animation_count // 4]
        self.heart_animation_count += 1

        if self.heart_animation_count >= len(self.heart_imgs) * 4:
            self.heart_animation_count = 0

        self.win.blit(self.heart_img, (self.width-60, 5))

    def draw_star(self):
        """
        Method for drawing star animation
        :return: None
        """
        self.star_img = self.star_imgs[self.star_animation_count // 4]
        self.star_animation_count += 1

        if self.star_animation_count >= len(self.star_imgs) * 4:
            self.star_animation_count = 0

        self.win.blit(self.star_img, (self.width-60, 50))

    def reset_game(self):
        """
        This method is used to reset all game values
        :return: None
        """
        self.start = True
        self.paused = True
        self.wave_turn = 0
        self.enemies = []
        self.towers = []
        self.support_towers = []
        self.budget = 1000
        self.lives = 8