import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    
    def __init__(self):
        """"Intialize game and draw screen"""
        pygame.init()
        self.settings = Settings()


        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption(self.settings.name)


        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg, (self.settings.screen_width, self.settings.screen_height))

        self.running = True
        #set up timer to control frame rate
        self.clock = pygame.time.Clock()
        #set up ship
        self.ship = Ship(self)


    def run_game(self):
        #Game loop
        while self.running:
            #call event listener function
            self._check_events()
            #call update screen function
            self._update_screen() 
            self.clock.tick(self.settings.FPS)


    def _update_screen(self):
        #draw background image to screen
        self.screen.blit(self.bg, (0, 0))
        #draw ship to screen and update display    
        self.ship.draw()
        pygame.display.flip()

    def _check_events(self):
        """Listener function Respond to keypresses and events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit() # Limit to 60 FPS


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
    
