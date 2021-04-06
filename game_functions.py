import sys
import pygame
def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(game_settings, screen, troll):
    screen.fill(game_settings.bg_color)
    troll.blitme()
    pygame.display.flip()