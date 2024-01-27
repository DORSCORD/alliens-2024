import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen

        #Download image alien and rect
        self.image = pygame.image.load("Image/alien.bmp")
        self.rect = self.image.get_rect()

        #Every alien spawn in left-up screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Save gorizontale position alien
        self.x = float(self.rect.x)
