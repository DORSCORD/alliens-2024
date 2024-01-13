import pygame


class Ship:
    """Клас для управління кораблем"""

    def __init__(self, ai_game):
        """Ініціалізує корабель та встановлює його початкову позицію"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #Завантаження зображення корабля і отримання прямокутника
        self.image = pygame.image.load("image/ship.bmp")
        self.rect = self.image.get_rect()
        #Кожен новий корабель зявляеться у нижній частині екрану
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Рисує корабель в поточні позиції"""
        self.screen.blit(self.image, self.rect)
        