import pygame

class Troll():
    def __init__(self, game_settings, screen):
        self.screen = screen
        self.game_settings = game_settings
        self.image = pygame.image.load("images/Troll.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right:
            self.center += self.game_settings.troll_speed_factor
        if self.moving_left:
            self.center -= self.game_settings.troll_speed_factor
        self.rect.centerx = self.center
    def blitme(self):
        self.screen.blit(self.image, self.rect)