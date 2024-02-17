class GameStats:
    """Відслідковування статистики гри"""

    def __init__(self, ai_game):
        """Ініціація статистики"""
        self.settings = ai_game.settings
        self.reset_stats()

        # Game started in no active 
        self.game_active = False

        # Рекорд гри
        self.hight_score = 0
    
    def reset_stats(self):
        """Ініціалізує статистику, що змінюється під час гри"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
