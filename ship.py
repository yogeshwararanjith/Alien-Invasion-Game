import pygame


class Ship:
    def __init__(self, screen):
        # Initialize the ship and set its starting position
        self.screen = screen

        # load the ship image and get its rect
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        # matching center of  x coordinate of ship with center of  x coordinate of screen
        self.rect.centerx = self.screen_rect.centerx
        # matching bottom of y coordinate of ship with bottom of y coordinate of screen
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        # Draw the ship at its current location
        # blit method draws image on the screen
        self.screen.blit(self.image, self.rect)
