import pygame

"""
MAKING SCREEN SQUARE SO THAT ALL CELL WILL BECOME SQUARE
"""
SCREEN_SIZE = 900

NUM_CELLS = 10
"""
MAKING BOARD SIZE EQUAL TO 70% WIDTH OF SCREEN SIZE
"""
BOARD_SIZE = int(SCREEN_SIZE * 0.7), int(SCREEN_SIZE * 0.7)
BOARD_POSITION = int(SCREEN_SIZE // 2 - BOARD_SIZE[0] // 2), int(
    SCREEN_SIZE // 2 - BOARD_SIZE[0] // 2
)
CELL_SIZE = BOARD_SIZE[0] // NUM_CELLS

"""
COLORS
"""
WHITE = (255, 255, 255, 255)
BLACK = (0, 0, 0, 255)


def update_alpha(color: tuple[int], alpha: int):
    return (*color[:3], alpha)
