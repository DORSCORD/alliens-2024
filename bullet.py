from typing import Any
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Клас для управлиння снарядами, який стриляе корабель"""

    def __init__(self, ai_game):
        """Створює обєкт снаряду в поточній позиції коробля"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #Створю' снаряд в позиції (0, 0) і призначемо правильну позицію
        self.rect = pygame.Rect(0, 0, self.settings.bulley_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Save bullet position in float
        self.y = float(self.rect.y)

    def update(self):
        """Move bullet in up for screen"""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Вивоже снаряд на екран"""
        pygame.draw.rect(self.screen, self.color, self.rect)
        