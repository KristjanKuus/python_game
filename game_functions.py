import sys
import pygame
from bullet import Bullet
from megusta import Megusta
from game_stats import GameStats
from time import sleep

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

BackGround = Background('images/rai.bmp', [0,0])

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
    screen.blit(BackGround.image, BackGround.rect)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    troll.blitme()
    megustas.draw(screen)
    pygame.display.flip()


def update_bullets(megustas, bullets, game_settings, screen, troll):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
        check_alien_collisons(megustas, bullets, game_settings, screen, troll)

def check_alien_collisons(megustas, bullets, game_settings, screen, troll):
    collisions = pygame.sprite.groupcollide(bullets, megustas, True, True)
    if len(megustas) == 0:
        bullets.empty()
        create_fleet(game_settings, screen, troll, megustas)

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

def check_fleet_edges(game_settings, megustas):
    for megusta in megustas.sprites():
        if megusta.check_edges():
            change_fleet_direction(game_settings, megustas)
            break
def change_fleet_direction(game_settings, megustas):
    for megusta in megustas.sprites():
        megusta.rect.y += game_settings.fleet_drop_speed
    game_settings.fleet_direction *= -1

def update_megustas(game_settings, stats, screen, troll, megustas, bullets):
    check_fleet_edges(game_settings, megustas)
    megustas.update()
    # Check collision between megustas and troll
    check_megustas_bottom(game_settings, stats, screen, troll, megustas, bullets)
    if pygame.sprite.spritecollideany(troll, megustas):
        troll_hit(game_settings, stats, screen, troll, megustas, bullets)

def troll_hit(game_settings, stats, screen, troll, megustas, bullets):
    stats.ship_left = stats.ships_left -1
    megustas.empty()
    bullets.empty()
    create_fleet(game_settings, screen, troll, megustas)
    troll.ship_center()

def check_megustas_bottom(game_settings, stats, screen, troll, megustas, bullets):
    screen_rect = game_settings.screen_height
    for megustas in megustas.sprites():
        if megustas.rect.bottom >= screen_rect:
            sys.exit()
