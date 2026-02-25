import pygame
class Snake:
    """A class to manage the snake"""
    def __init__(self, pi_game):
        """Initialize the snake and set it's starting position"""
        self.screen = pi_game.screen
        self.screen_rect = pi_game.screen.get_rect()

        #Load snake image and get its rect
        self.image = pygame.image.load('images/snake.bmp')
        self.rect = self.image.get_rect()

        #Start each new snake at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw the snake at its current location"""
        self.screen.blit(self.image, self.rect)


