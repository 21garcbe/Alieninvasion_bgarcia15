import pygame
from typing import TYPE_CHECKING
from pygame.sprite import Sprite

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Bullet(Sprite):
    def __init__(self, game: 'AlienInvasion'):
        super().__init__()
        self.game = game
        self.settings = game.settings
        self.screen = game.screen

        self.image = pygame.image.load(self.settings.bullet_file)
        self.image = pygame.transform.scale(self.image, (self.settings.bullet_width, self.settings.bullet_height))
        self.rect = self.image.get_rect()
        self.rect.midtop = game.ship.rect.midtop
        self.y_pos = float(self.rect.y)
    
    def update(self):
        self.y_pos -= self.settings.bullet_speed
        self.rect.y = self.y_pos

    def draw_bullet(self):
        self.screen.blit(self.image, self.rect)