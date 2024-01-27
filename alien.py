from typing import Any
import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Клас для прибульця"""

    def __init__(self, ai_game):
        """Ініціалізує прибульця та задає його початкову позицію"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Завантаження зображення прибульця та визначення rect
        self.image = pygame.image.load("Image/alien.bmp")
        self.rect = self.image.get_rect()

        # Кожен новий прибулець з'являється в лівому верхньому куті екрану
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Збереження точної горизонтальної позиції прибульця
        self.x = float(self.rect.x)

    def check_edges(self):
        """Retuen True if alien with end screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Переміщує прибулця праворуч"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x