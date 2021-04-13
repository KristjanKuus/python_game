import sys
import pygame
from bullet import Bullet
from megusta import Megusta

def check_keydown_events(event, game_settings, screen, troll, bullets):
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        troll.moving_right = True
    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
        troll.moving_left = True
    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
        troll.moving_down = True
    if event.key == pygame.K_UP or event.key == pygame.K_w:
        troll.moving_up = True
    if event.key == pygame.K_SPACE:
        fire_bullet(game_settings, screen, troll, bullets)
    if event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, troll):
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        troll.moving_right = False
    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
        troll.moving_left = False
    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
        troll.moving_down = False
    if event.key == pygame.K_UP or event.key == pygame.K_w:
        troll.moving_up = False


def check_events(game_settings, screen, troll, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, game_settings, screen, troll, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, troll)


def update_screen(game_settings, screen, troll, megustas, bullets):
    screen.fill(game_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    troll.blitme()
    megustas.draw(screen)
    pygame.display.flip()


def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def fire_bullet(game_settings, screen, troll, bullets):
    if len(bullets) < game_settings.bullets_allowed:
        new_bullet = Bullet(game_settings, screen, troll)
        bullets.add(new_bullet)

def create_fleet(game_settings, screen, megustas):
    megusta = Megusta(game_settings, screen)
    megusta_width = megusta.rect.width
    available_space_x = game_settings.screen_width - 2 * megusta_width
    number_megusta_x = int(available_space_x / (2 * megusta_width))
    for megusta_number in range(number_megusta_x):
        megusta = Megusta(game_settings, screen)
        megusta.x = megusta_width + 2 * megusta_width * megusta_number
        megusta.rect.x = megusta.x
        megustas.add(megusta)