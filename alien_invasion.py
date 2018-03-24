import pygame
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
    # Инициализирует pygame, settings и объект экрана
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                     ai_settings.screen_height))
    pygame.display.set_caption("Нашествие пришельцев")

    # Создание кнопки Play
    play_button = Button(ai_settings, screen, "Играть")

    # Создание экземпляра для хранения игровой статистики.
    stats = GameStats(ai_settings)

    #Создание экземпляра Scoreboard.
    sb = Scoreboard(ai_settings, screen, stats)

    # Создание корабля
    ship = Ship(ai_settings, screen)

    # Создание группы пуль и группы пришельцев.
    bullets = Group()
    aliens = Group()

    # Создание флота пришельцев.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Запуск основоного цикла игры
    while True:
        # Отслеживание клавиатуры и мыши
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship,
                        aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship,
                                  aliens, bullets)
            gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets,
                             play_button)


run_game()
