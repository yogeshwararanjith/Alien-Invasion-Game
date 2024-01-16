import sys
import pygame
from settings import Settings
from ship import Ship

def run_game():
    # Initialize game and create an object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(screen)

    # start the main loop for the game
    while True:

        # watch for keyboard and mouse events

        # This is a submodule of Pygame that deals with events.
        # In Pygame, an event is something that happens, such as a key press, mouse movement, or window resize.

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Redraw the screen during each pass through the loop.
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        #  Make the most recently drawn screen visible.
        pygame.display.flip()

run_game()
