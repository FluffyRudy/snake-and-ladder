import pygame
from pygame.math import Vector2
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

        max_y_limit = BOARD_POSITION[1] + BOARD_SIZE[1] - CELL_SIZE
        full_rel_height = pos[1] + self.image.get_height()
        posy_clipped = (
            pos[1]
            if full_rel_height <= max_y_limit
            else max_y_limit - self.image.get_height()
        )

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
        """only deal with bottom rect"""
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
        """red area is actual size of image"""
        # pygame.draw.rect(display_surface, "red", self.rect, 5)
        pygame.draw.rect(display_surface, "blue", self.head_rect, 5)
        pygame.draw.rect(display_surface, "green", self.tail_rect, 5)
