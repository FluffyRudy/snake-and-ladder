from settings import BOARD_POSITION, BOARD_SIZE, CELL_SIZE
import pygame


def get_head_point(image: pygame.Surface, rect: pygame.Rect) -> pygame.Rect:
    """
    Find the head point of the snake, defined as the topmost non-transparent pixel in the first row of the image.

    Args:
        image (pygame.Surface): The image surface containing the snake.
        rect (pygame.Rect): The rectangular area of the image to be checked.

    Returns:
        pygame.Rect: A rectangle representing the head point of the snake, aligned to the grid.
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


def get_tail_point(image: pygame.Surface, rect: pygame.Rect) -> pygame.Rect:
    """
    Find the tail point of the snake, defined as the bottommost non-transparent pixel in the last row of the image.

    Args:
        image (pygame.Surface): The image surface containing the snake.
        rect (pygame.Rect): The rectangular area of the image to be checked.

    Returns:
        pygame.Rect: A rectangle representing the tail point of the snake, aligned to the grid.
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


def convert_coordinate(
    coordinates: tuple[int, int], size: tuple[int, int]
) -> tuple[int, int]:
    """
    Convert logical coordinates to screen coordinates.

    Args:
        coordinates (tuple[int, int]): The logical coordinates (x, y) to be converted.
        size (tuple[int, int]): The size (width, height) of the element being positioned.

    Returns:
        tuple[int, int]: The converted screen coordinates (x, y).
    """
    offset_x, offset_y = BOARD_POSITION
    width, height = BOARD_SIZE
    return (
        offset_x + coordinates[0] * CELL_SIZE,
        offset_y + height + coordinates[1] * CELL_SIZE - size[1],
    )
