import pygame
from pygame.sprite import Sprite, Group
from random import randrange
from settings import SNAKES, CELL_SIZE, BOARD_POSITION, BOARD_SIZE


class Snake(Sprite):
    snakes = SNAKES.copy()

    def __init__(self, pos: tuple[int, int], group: Group):
        super().__init__(group)
        random_index = randrange(0, len(self.snakes))
        self.image = pygame.image.load(self.snakes.pop(random_index))
        if self.image.get_height() <= CELL_SIZE:
            self.image = pygame.transform.scale2x(self.image)

        """clip y position within the board"""
        max_y_limit = BOARD_POSITION[1] + BOARD_SIZE[1] - CELL_SIZE
        full_rel_height = pos[1] + self.image.get_height()
        posy_clipped = (
            pos[1]
            if full_rel_height <= max_y_limit
            else max_y_limit - self.image.get_height()
        )

        """clip x position within the board"""
        max_x_limit = BOARD_POSITION[0] + BOARD_SIZE[0]
        full_rel_width = pos[0] + self.image.get_width()
        posx_clipped = (
            pos[0]
            if full_rel_width <= max_x_limit
            else max_x_limit - self.image.get_width()
        )

        self.rect = self.image.get_rect(topleft=(posx_clipped, posy_clipped))
        self.head_rect = self.get_head_point()
        self.tail_rect = self.get_tail_point()

    def get_head_point(self):
        """
        find the head point of the snake (topmost non-transparent pixel in the first row).
        """
        for y in range(CELL_SIZE):
            for x in range(self.rect.width):
                if self.image.get_at((x, y))[3] != 0:
                    grid_x = (
                        self.rect.left + x - BOARD_POSITION[0]
                    ) // CELL_SIZE * CELL_SIZE + BOARD_POSITION[0]
                    grid_y = (
                        self.rect.top + y - BOARD_POSITION[1]
                    ) // CELL_SIZE * CELL_SIZE + BOARD_POSITION[1]
                    return pygame.Rect(grid_x, grid_y, CELL_SIZE, CELL_SIZE)
        return pygame.Rect(0, 0, CELL_SIZE, CELL_SIZE)

    def get_tail_point(self):
        """
        find the tail point of the snake (bottommost non-transparent pixel in the last row).
        """
        for y in range(self.rect.height - 1, self.rect.height - CELL_SIZE - 1, -1):
            for x in range(self.rect.width):
                if self.image.get_at((x, y))[3] != 0:
                    grid_x = (
                        self.rect.left + x - BOARD_POSITION[0]
                    ) // CELL_SIZE * CELL_SIZE + BOARD_POSITION[0]
                    grid_y = (
                        self.rect.top + y - BOARD_POSITION[1]
                    ) // CELL_SIZE * CELL_SIZE + BOARD_POSITION[1]
                    return pygame.Rect(grid_x, grid_y, CELL_SIZE, CELL_SIZE)
        return pygame.Rect(0, 0, CELL_SIZE, CELL_SIZE)

    def update(self, display_surface: pygame.Surface):
        """Draw the head and tail points for debugging."""
        pygame.draw.rect(display_surface, "blue", self.head_rect, 5)
        pygame.draw.rect(display_surface, "green", self.tail_rect, 5)
