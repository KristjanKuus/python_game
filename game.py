
import pygame
from settings import Settings
from troll import Troll
from megusta import Megusta
import game_functions as gf
from pygame.sprite import Group

def run_game():
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width,game_settings.screen_height))
    pygame.display.set_caption("U Mad Bro?")

    troll = Troll(game_settings, screen)
    bullets = Group()
    megusta = Megusta(game_settings, screen)
    while True:
        gf.check_events(game_settings, screen, troll, bullets)
        troll.update()
        gf.update_bullets(bullets)
        gf.update_screen(game_settings, screen, troll, megusta, bullets)

run_game()