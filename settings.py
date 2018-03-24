class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""
    def __init__(self):
        """Инициализирует настройку игры"""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Параметры пули
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # Настройки пришельцев.
        self.fleet_drop_speed = 10

        # fleet_direction = 1 обозначают движение в право, а -1 - влево.
        self.fleet_direction = 1

        # Настройки корабля
        self.ship_limit = 3

        # Темп ускорения игры
        self.speedup_scale = 1.1
        self.aliens_points_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.3
        self.bullet_speed_factor = 1.5
        self.alien_speed_factor = 1.1

        # Подсчет очков.
        self.aliens_points = 10

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.aliens_points = int(self.aliens_points * self.aliens_points_scale)
