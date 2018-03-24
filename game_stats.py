class GameStats:
    """Отслеживание статистики для игры Alien Invasion."""

    def __init__(self, ai_settings):
        """Инициализирует статистику"""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.high_score = 0

        # Игра запускается в активном состоянии.
        self.game_active = False

    def reset_stats(self):
        """Инициализирует ститистику, изменяющуюся в ходе игры."""
        self.ship_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
