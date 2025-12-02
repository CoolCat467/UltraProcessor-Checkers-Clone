import pygame
from DrawBoard import draw_board


def configure_size(screen, board):
    if not hasattr(configure_size, "previous_square_size"):
        configure_size.previous_square_size = -1

    width, height = pygame.display.get_surface().get_size()
    square_size = min(width, height) // 8

    board_size_pixels = square_size * 8
    margin_x = (width - board_size_pixels) // 2
    margin_y = (height - board_size_pixels) // 2

    board_surface = None
    if square_size != configure_size.previous_square_size:
        board_surface = draw_board(board, square_size)
        configure_size.previous_square_size = square_size

    return board_surface, margin_x, margin_y, square_size


def get_square_size():
    window_width, window_height = 640, 640

    window_width, window_height = pygame.display.get_surface().get_size()
    square_size = min(window_width, window_height) // 8

    return square_size


def get_window_dimensions():
    window_width, window_height = pygame.display.get_surface().get_size()

    return window_width, window_height