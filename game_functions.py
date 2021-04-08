import sys
import pygame
from bullet import Bullet
def check_keydown_events(event, game_settings, screen, troll, bullets):
    if event.key == pygame.K_RIGHT:
        troll.moving_right = True
    if event.key == pygame.K_LEFT:
        troll.moving_left = True
    if event.key == pygame.K_DOWN:
        troll.moving_down = True
    if event.key == pygame.K_UP:
        troll.moving_up = True
    if event.key == pygame.K_SPACE:
        if len(bullets) < game_settings.bullets_allowed:
            new_bullet = Bullet(game_settings, screen,troll)
            bullets.add(new_bullet)

def check_keyup_events(event, troll):
    if event.key == pygame.K_RIGHT:
        troll.moving_right = False
    if event.key == pygame.K_LEFT:
        troll.moving_left = False
    if event.key == pygame.K_DOWN:
        troll.moving_down = False
    if event.key == pygame.K_UP:
        troll.moving_up = False

def check_events(game_settings, screen, troll, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, game_settings, screen, troll, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, troll)

def update_screen(game_settings, screen, troll, bullets):
    screen.fill(game_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    troll.blitme()
    pygame.display.flip()