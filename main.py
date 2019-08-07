"""
@author: Argert Boja
@org: ABEnt
@date: May 2019
@description: This project aims implementation of several
              python games in order to get some basic experience
              on python programming
"""

# import packages
import os
import pygame

# import classes
from tower_defense.tower_defense_game import TowerDefenseGame

# images
icon = pygame.transform.scale(pygame.image.load(os.path.join("images", "icon.png")),(32,32))
bg = pygame.image.load(os.path.join("images", "bg.jpg"))
td_icon = pygame.image.load(os.path.join("images", "td1.png"))
td_icon_hover = pygame.image.load(os.path.join("images", "td2.png"))
quit_confirmation_image = pygame.image.load(os.path.join("images", "quit_confirmation.png"))
yes_icon = pygame.image.load(os.path.join("images", "yes.png"))
yes_icon_hover = pygame.image.load(os.path.join("images", "yes_hover.png"))
no_icon = pygame.image.load(os.path.join("images", "no.png"))
no_icon_hover = pygame.image.load(os.path.join("images", "no_hover.png"))

# initialize pygame
pygame.init()
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100, 100)
pygame.display.set_icon(icon)
pygame.display.set_caption("Python Game Collection")

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

# Main menu and class
class Main:

    def __init__(self):
        self.width = 1000
        self.height = 600
        self.win = pygame.display.set_mode((self.width, self.height))
        self.bg = bg
        self.buttons = []
        self.buttons.append(Button(200, 200, td_icon, td_icon_hover, "tower_defense"))
        self.quitting = False
        self.exit = False
        self.yes_button = None
        self.no_button = None

    def run(self):
        """
        This is the engine for the game
        :return: None
        """
        run = True
        while run:
            # Get mouse position
            if not(self.exit):
                mouse_x, mouse_y = pygame.mouse.get_pos()

            # Check events
            for event in pygame.event.get():
                if event.type == pygame.QUIT and not (self.quitting):
                    self.quitting = True
                    break

                if event.type == pygame.MOUSEBUTTONDOWN:
                    for button in self.buttons:
                        if button.click(mouse_x, mouse_y):
                            if button.name == "tower_defense":
                                self.exit = True
                                self.yes_button = None
                                self.no_button = None
                                game = TowerDefenseGame()
                                game.run()
                                run = False
                    if self.yes_button is not None and self.yes_button.click(mouse_x, mouse_y):
                        run = False

                    if self.no_button is not None and self.no_button.click(mouse_x, mouse_y):
                        self.quitting = False
            if not(self.exit):
                # draw images
                self.draw()

            # draw quitting confirmation menu
            if self.quitting and not (self.exit):
                self.draw_confirmation_menu(360, 300, mouse_x, mouse_y)

            if not(self.exit):
                pygame.display.update()
        pygame.quit()

    def draw(self):
        """
        Draw background and buttons
        :return: None
        """

        # Draw background
        try:
            self.win.blit(self.bg, (0,0))
        except:
            print("exeption")

        # Get mouse position
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Draw buttons
        for button in self.buttons:
            button.draw(self.win)
            button.mouse_hover(mouse_x, mouse_y)

    def draw_confirmation_menu(self, x, y, mouse_x, mouse_y):
        """
        This method draws confirmation menu if user wants to quit
        :param x: x position of menu
        :param y: y position of menu
        :param mouse_x: x position of mouse
        :param mouse_y: y position of mouse
        :return: None
        """

        # draw background image of menu
        self.win.blit(quit_confirmation_image, (x, y))

        # generate yes and no buttons
        self.yes_button = Button(x + 40, y + 130, yes_icon, yes_icon_hover, "yes")
        self.no_button = Button(x + 190, y + 130, no_icon, no_icon_hover, "no")
        self.yes_button.mouse_hover(mouse_x, mouse_y)
        self.no_button.mouse_hover(mouse_x, mouse_y)
        self.yes_button.draw(self.win)
        self.no_button.draw(self.win)

# run main class
main_screen = Main()
main_screen.run()
