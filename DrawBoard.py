import pygame

LIGHT_BROWN = (238, 180, 125)  # Light brown color for squares
DARK_BROWN = (123, 63, 0)  # Dark brown color for squares
BLACK = (0, 0, 0)
RED = (255, 0, 0)

def draw_board(board, square_size):
    surface = pygame.Surface((square_size * 8, square_size * 8))

    row = 0
    while row < 8:
        col = 0
        while col < 8:
            if (row + col) % 2 == 0:
                square_color = DARK_BROWN
                rect = pygame.Rect(col * square_size, row * square_size, square_size, square_size)

                pygame.draw.rect(surface, square_color, rect)

            else:
                square_color = LIGHT_BROWN
                rect = pygame.Rect(col * square_size, row * square_size, square_size, square_size)

                pygame.draw.rect(surface, square_color, rect)

            # Draw the pieces, if any
            piece = board[row][col + 1]
            radius = square_size // 2 - 5
            center_x = col * square_size + square_size // 2
            center_y = row * square_size + square_size // 2

            if piece == 'R':
                pygame.draw.circle(surface, RED, (center_x, center_y), radius)
            elif piece == 'B':
                pygame.draw.circle(surface, BLACK,(center_x, center_y), radius)

            col = col + 1
        row = row + 1

    return surface