import sys

import pygame


class AlienInvasion:
    """Клас для управління ресурсами та поведінкою гри"""

    def __init__(self):
        """Інцилізацує гру та створює ігрові ресурси"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Запуск основного циклу гри"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            pygame.display.flip()

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()