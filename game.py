
import pygame
from settings import Settings
from troll import Troll
import game_functions as gf

def run_game():
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width,game_settings.screen_height))
    pygame.display.set_caption("U Mad Bro?")

    troll = Troll(screen)

    while True:
        gf.check_events(troll)
        troll.update()
        gf.update_screen(game_settings, screen, troll)

run_game()