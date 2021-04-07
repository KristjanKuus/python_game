import sys
import pygame
def check_keydown_events(event, troll):
    if event.key == pygame.K_RIGHT:
        troll.moving_right = True
    if event.key == pygame.K_LEFT:
        troll.moving_left = True

def check_keyup_events(event, troll):
    if event.key == pygame.K_RIGHT:
        troll.moving_right = False
    if event.key == pygame.K_LEFT:
        troll.moving_left = False

def check_events(troll):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, troll)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, troll)

def update_screen(game_settings, screen, troll):
    screen.fill(game_settings.bg_color)
    troll.blitme()
    pygame.display.flip()