import pygame

class TowerDefenseGame:

    def __init__(self):
        self.width = 1000
        self.height = 800
        self.win = pygame.display.set_mode((self.width, self.height))

    def run_twer_defense_game(self):
        run = True

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

        pygame.quit()