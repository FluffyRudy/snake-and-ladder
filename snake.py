import pygame
import numpy
from pygame.sprite import Sprite, Group
from random import randrange
from settings import SNAKES, CELL_SIZE, BOARD_POSITION


class Snake(Sprite):
    snakes = SNAKES.copy()

    def __init__(self, pos: tuple[int, int], group: Group):
        super().__init__(group)
        random_index = randrange(0, len(self.snakes))
        self.image = pygame.image.load(self.snakes.pop(random_index))
        if self.image.get_height() <= CELL_SIZE:
            self.image = pygame.transform.scale2x(self.image)
        self.rect = self.image.get_rect(topleft=pos)
        self.head_rect = self.get_head_point()
        self.tail_rect = self.get_tail_point()
        print(self.head_rect, self.tail_rect, self.rect)

    def get_head_point(self):
        """
        only deal with top rect
        """
        start_x, end_x = 0, self.rect.width
        start_y, end_y = 0, CELL_SIZE

        color_pos = (0, 0)
        for y in range(start_y, end_y):
            for x in range(start_x, end_x):
                if self.image.get_at((x, y))[3] != 0:
                    color_pos = x, y
                    break
            if color_pos != (0, 0):
                break

        return pygame.Rect(
            self.rect.left + (color_pos[0] // CELL_SIZE) * CELL_SIZE,
            self.rect.top + (color_pos[1] // CELL_SIZE) * CELL_SIZE,
            CELL_SIZE,
            CELL_SIZE,
        )

    def get_tail_point(self):
        start_x, end_x = 0, self.rect.width
        start_y, end_y = self.rect.height - 1, self.rect.height - 1 - CELL_SIZE

        color_pos = (0, 0)
        for y in range(start_y, end_y, -1):
            for x in range(start_x, end_x):
                if self.image.get_at((x, y))[3] != 0:
                    color_pos = x, y
                    break
            if color_pos != (0, 0):
                break

        y = (
            self.rect.bottom
            - ((self.rect.height - color_pos[1]) // CELL_SIZE) * CELL_SIZE
        )

        adjusted_y = (
            BOARD_POSITION[1]
            + ((y + CELL_SIZE - BOARD_POSITION[1]) // CELL_SIZE) * CELL_SIZE
        )

        return pygame.Rect(
            self.rect.left + (color_pos[0] // CELL_SIZE) * CELL_SIZE,
            adjusted_y - CELL_SIZE,
            CELL_SIZE,
            CELL_SIZE,
        )

    def update(self, display_surface: pygame.Surface):
        pygame.draw.rect(display_surface, "red", self.rect, 3)
        pygame.draw.rect(display_surface, "blue", self.head_rect, 3)
        pygame.draw.rect(display_surface, "blue", self.tail_rect, 3)
