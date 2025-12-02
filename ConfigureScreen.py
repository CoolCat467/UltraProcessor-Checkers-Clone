
import pygame

# Constants
BLACK = (0, 0, 0)

def configure_screen():
    window_width, window_height = 640, 640

    pygame.display.set_caption("Checkers Game")
    screen = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)

    return screen


def color_screen_black(screen):
    screen.fill(BLACK)

    return screen

