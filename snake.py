from settings import SNAKES, CELL_SIZE, BOARD_POSITION, BOARD_SIZE
import pygame
from pygame.math import Vector2
from pygame.sprite import Sprite, Group
from random import randrange
from board_util import get_head_point, get_tail_point


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
        self.head_rect = get_head_point(self.image, self.rect)
        self.tail_rect = get_tail_point(self.image, self.rect)
        self.throw_pawns_coor = (
            Vector2(self.tail_rect.topleft) - Vector2(self.head_rect.topleft)
        ) // CELL_SIZE
        self.throw_pawns_coor.x = int(self.throw_pawns_coor.x)
        self.throw_pawns_coor.y = int(self.throw_pawns_coor.y)

    def update(self, display_surface: pygame.Surface):
        """Draw the head and tail points for debugging."""
        pygame.draw.rect(display_surface, "blue", self.head_rect, 5)
        pygame.draw.rect(display_surface, "green", self.tail_rect, 5)
