import sys
import pygame
from settings import Settings
from snake import Snake
class PythonInvasion:
    """Overall class to manage game assets and behavior"""
    def __init__(self):
        """Initialize the game and create game resources"""
        #Considered to be the on switch for the library. Initializes background settings needed to work properly
        pygame.init
        #Clock used to ensure game runs at same speed on all machines
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        #Creates a display window that is 1200 pixels wide and 800 pixels tall
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Python Invasion")
        self.snake = Snake(self)
        #Set BG color
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Starts the main loop for the game"""
        while True:
            self._check_events()
            self.snake.update()
            self._update_screen()
            #Tells pygame to ensure the loop runs 60 times per second
            self.clock.tick(60)
    
    #Helper function for checking for events.
    def _check_events(self):
         # Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit() 
                elif event.type == pygame.KEYDOWN:
                     if event.key == pygame.K_RIGHT:
                          #Move the snake to the right
                          self.snake.moving_right = True
                     elif event.key == pygame.K_LEFT:
                          self.snake.moving_left = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                         self.snake.moving_right = False
                    elif event.key == pygame.K_LEFT:
                         self.snake.moving_left = False
                                     
    #Helper function for screen updates.
    def _update_screen (self):
         #Fills screen with the BG color    
            self.screen.fill(self.settings.bg_color)  
            self.snake.blitme()
            #Makes the most recently drawn screen visible
            pygame.display.flip()


if __name__ == '__main__':
    """Makes a game instance and runs the game"""
    pi = PythonInvasion()
    pi.run_game()

    

