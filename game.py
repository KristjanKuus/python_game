
import pygame
from settings import Settings
from troll import Troll
from megusta import Megusta
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button

def run_game():
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width,game_settings.screen_height))
    pygame.display.set_caption("U Mad Bro?")
    play_button = Button(game_settings, screen, "PLAY")
    stats = GameStats(game_settings)

    troll = Troll(game_settings, screen)
    bullets = Group()
    megustas = Group()
    gf.create_fleet(game_settings, screen, troll, megustas)
    while True:
        gf.check_events(game_settings, screen, troll, bullets, stats, play_button)
        gf.update_screen(game_settings, screen, troll, megustas, bullets, play_button, stats)
        if stats.game_active == True:
            troll.update()
            gf.update_bullets(megustas, bullets, game_settings, screen, troll)
            gf.update_megustas(game_settings, stats, screen, troll, megustas, bullets)


run_game()