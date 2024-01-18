import sys
import pygame

def check_events(ship):

    # responds to key press and mouse events
    # watch for keyboard and mouse events
    # This is a submodule of Pygame that deals with events.
    # In Pygame, an event is something that happens, such as a key press, mouse movement, or window resize.

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # KEYDOWN is pressing the key
        # KEYUP is when key is released
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)


def check_keydown_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def update_screen(ai_settings,screen,ship):
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    #  Make the most recently drawn screen visible.
    pygame.display.flip()
