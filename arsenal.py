from typing import TYPE_CHECKING
import pygame
from bullet import Bullet

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion



class Arsenal:
    """A class to manage the arsenals of weapons."""
    
    def __init__(self, game: 'AlienInvasion'):
        """Initialize the ship's arsenal."""
        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()

    def update_arsenal(self):
        self.arsenal.update()
        self._remove_offscreen_bullets()
    
    def _remove_offscreen_bullets(self):
        for bullet in self.arsenal.copy():
            #remove bullet if it has moved off the top of the screen
            if bullet.rect.bottom <= 0:
                self.arsenal.remove(bullet)

    def draw(self):
        for bullet in self.arsenal:
            bullet.draw_bullet()
    
    def fire_bullet(self):
        if len(self.arsenal) < self.settings.bullet_amount:
            new_bullet = Bullet(self.game)
            self.arsenal.add(new_bullet)
            return True
        return False
    
        

