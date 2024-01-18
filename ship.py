import pygame


class Ship:
    def __init__(self, screen, ai_settings):
        # Initialize the ship and set its starting position
        self.screen = screen
        self.ai_settings = ai_settings
        # load the ship image and get its rect
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        # matching center of  x coordinate of ship with center of  x coordinate of screen
        self.rect.centerx = self.screen_rect.centerx
        # matching bottom of y coordinate of ship with bottom of y coordinate of screen
        self.rect.bottom = self.screen_rect.bottom

        #store a decimal value for the ships center
        self.center = float(self.rect.centerx)
        # movement flag
        self.moving_right = False
        self.moving_left = False
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # update the rect object
        self.rect.centerx = self.center

    def blitme(self):
        # Draw the ship at its current location
        # blit method draws image on the screen
        self.screen.blit(self.image, self.rect)


