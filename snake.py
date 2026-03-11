import pygame
class Snake:
    """A class to manage the snake"""
    def __init__(self, pi_game):
        """Initialize the snake and set it's starting position"""
        self.screen = pi_game.screen
        self.settings = pi_game.settings
        self.screen_rect = pi_game.screen.get_rect()

        #Load snake image and get its rect
        self.image = pygame.image.load('images/snake.bmp')
        self.rect = self.image.get_rect()

        #Start each new snake at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        #Stores a float(value with a .) for the snake's exact horizontal position.
        self.x = float(self.rect.x)

        #Start with a ship that's not moving
        self.moving_right = False
        self.moving_left = False

        
    
    #Checks to see if moving is True and moves the char accordingly
    def update(self):
        #Updates the snake's x value, not the rect
        if self.moving_right:
            self.x += self.settings.snake_speed
        if self.moving_left:
            self.x -= self.settings.snake_speed
        #Updates the rect object from self.x
        self.rect.x = self.x
    
    def blitme(self):
        """Draw the snake at its current location"""
        self.screen.blit(self.image, self.rect)


