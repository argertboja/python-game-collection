import os

import pygame

from tower_defense.tower_defense_game import TowerDefenseGame

icon = pygame.transform.scale(pygame.image.load(os.path.join("images", "icon.png")),(32,32))


class Main:
    def __init__(self):
        pygame.init()
        self.width = 1000
        self.height = 600
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100,100)
        pygame.display.set_icon(icon)
        self.win = pygame.display.set_mode((self.width, self.height))
        self.bg = pygame.image.load(os.path.join("images", "bg.jpg"))
        self.td1 = pygame.image.load(os.path.join("images", "td1.png"))
        self.td2 = pygame.image.load(os.path.join("images", "td2.png"))

    def run(self):
        run = True

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            self.draw()

    def draw(self):
        self.win.blit(self.bg, (0,0))
        self.win.blit(self.td1, (200,200))
        mouse_x , mouse_y = pygame.mouse.get_pos()
        if (325 < mouse_x and mouse_x < 665) and (200 < mouse_y and mouse_y < 270):
            self.win.blit(self.td2, (200, 200))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    td_game = TowerDefenseGame()
                    td_game.run()
        pygame.init()
        pygame.display.update()

game = Main()
game.run()
