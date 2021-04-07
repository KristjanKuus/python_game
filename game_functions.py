import sys
import pygame
def check_events(troll):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                troll.rect.centerx += 1

def update_screen(game_settings, screen, troll):
    screen.fill(game_settings.bg_color)
    troll.blitme()
    pygame.display.flip()