
import pygame
from settings import Settings
from troll import Troll
import game_functions as gf
from pygame.sprite import Group

def run_game():
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width,game_settings.screen_height))
    pygame.display.set_caption("U Mad Bro?")

    troll = Troll(game_settings, screen)
    bullets = Group()

    while True:
        gf.check_events(game_settings, screen, troll, bullets)
        troll.update()
        bullets.update()
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        gf.update_screen(game_settings, screen, troll, bullets)

run_game()