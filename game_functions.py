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

def get_number_megustas_x(game_settings, megusta_width):
    available_space_x = game_settings.screen_width - 2 * megusta_width
    number_megusta_x = int(available_space_x / (2 * megusta_width))
    return number_megusta_x

def get_number_rows(game_settings, troll_height, megusta_height):
    available_space_y = game_settings.screen_height - 3 * megusta_height - troll_height
    number_rows = int(available_space_y / (2 *  megusta_height))
    return number_rows

def create_megusta(game_settings, screen, megustas, megusta_number, row_number):
    megusta = Megusta(game_settings, screen)
    megusta_width = megusta.rect.width
    megusta.x = megusta_width + 2 * megusta_width * megusta_number
    megusta.rect.x = megusta.x
    megusta.rect.y = megusta.rect.height + 2 * megusta.rect.height * row_number
    megustas.add(megusta)

def create_fleet(game_settings, screen, troll, megustas):
    megusta = Megusta(game_settings, screen)
    number_megustas_x = get_number_megustas_x(game_settings, megusta.rect.width)
    number_rows = get_number_rows(game_settings, troll.rect.height, megusta.rect.height)
    for row_number in range(number_rows):
        for megusta_number in range(number_megustas_x):
            create_megusta(game_settings, screen, megustas, megusta_number, row_number)

def update_megustas(megustas):
    megustas.update()