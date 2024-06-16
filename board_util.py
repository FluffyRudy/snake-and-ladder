from settings import BOARD_POSITION, BOARD_SIZE, CELL_SIZE
import pygame


def get_head_point(image: pygame.Surface, rect: pygame.Rect):
    """
    find the head point of the snake (topmost non-transparent pixel in the first row).
    """
    for y in range(CELL_SIZE):
        for x in range(rect.width):
            if image.get_at((x, y))[3] != 0:
                grid_x = (
                    rect.left + x - BOARD_POSITION[0]
                ) // CELL_SIZE * CELL_SIZE + BOARD_POSITION[0]
                grid_y = (
                    rect.top + y - BOARD_POSITION[1]
                ) // CELL_SIZE * CELL_SIZE + BOARD_POSITION[1]
                return pygame.Rect(grid_x, grid_y, CELL_SIZE, CELL_SIZE)
    return pygame.Rect(0, 0, CELL_SIZE, CELL_SIZE)


def get_tail_point(image: pygame.Surface, rect: pygame.Rect):
    """
    find the tail point of the snake (bottommost non-transparent pixel in the last row).
    """
    for y in range(rect.height - 1, rect.height - CELL_SIZE - 1, -1):
        for x in range(rect.width):
            if image.get_at((x, y))[3] != 0:
                grid_x = (
                    rect.left + x - BOARD_POSITION[0]
                ) // CELL_SIZE * CELL_SIZE + BOARD_POSITION[0]
                grid_y = (
                    rect.top + y - BOARD_POSITION[1]
                ) // CELL_SIZE * CELL_SIZE + BOARD_POSITION[1]
                return pygame.Rect(grid_x, grid_y, CELL_SIZE, CELL_SIZE)
    return pygame.Rect(0, 0, CELL_SIZE, CELL_SIZE)
