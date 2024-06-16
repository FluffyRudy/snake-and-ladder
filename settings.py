import os
import pygame
from random import randint as rint
from path_util import join, iterate_files, GRAPHICS_DIRECTORY

PROJECT_DIR = os.path.dirname(__file__)

"""
MAKING SCREEN SQUARE SO THAT ALL CELL WILL BECOME SQUARE
"""
SCREEN_SIZE = 1000

NUM_CELLS = 10
"""
MAKING BOARD SIZE EQUAL TO 70% WIDTH OF SCREEN SIZE
"""
BOARD_SIZE = int(SCREEN_SIZE * 0.7), int(SCREEN_SIZE * 0.7)
BOARD_POSITION = int(SCREEN_SIZE // 2 - BOARD_SIZE[0] // 2), int(
    SCREEN_SIZE // 2 - BOARD_SIZE[0] // 2
)
CELL_SIZE = BOARD_SIZE[0] // NUM_CELLS
BOARDER_RADIUS = 5
BORDER_WIDTH = 1

"""
COLORS
"""
WHITE = (255, 255, 255, 255)
BLACK = (0, 0, 0, 255)
RED = (255, 0, 0, 255)

"PAWNS"
MAX_PAWNS = 4
PAWN_SIZE = CELL_SIZE - 10

"DICE"
DICE_SPEED_DECREASE_FACTOR = 0.98
DICE_ANIMATION_SPEED = 0.1

"SNAKE"
snake = join(GRAPHICS_DIRECTORY, "snake")
SNAKES = iterate_files(snake)


def update_alpha(color: tuple[int], alpha: int):
    return (*color[:3], alpha)


def random_rgb_color() -> tuple[int, int, int]:
    return rint(0, 255), rint(0, 255), rint(0, 255)


def normalized_color(i: int, N: int):
    r = int((i / N) * 255)
    g = int((1 - (i / N)) * 255)
    b = 128
    return r, g, b
