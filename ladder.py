from typing import Any, Literal
from settings import (
    SMALL_BROWN_LADDER,
    SMALL_WHITE_LADDER,
    MID_LADDER,
    LARGE_LADDER,
    CELL_SIZE,
)
from path_util import GRAPHICS_DIRECTORY, join
import pygame
from pygame.math import Vector2
from pygame.sprite import Group, Sprite
from board_util import get_head_point, get_tail_point, convert_coordinate

LadderType = Literal[SMALL_BROWN_LADDER, SMALL_WHITE_LADDER, MID_LADDER, LARGE_LADDER]


class Ladder(Sprite):
    def __init__(
        self,
        coor: tuple[int, int],
        group: Group,
        type_: LadderType,
        scale_ratio: tuple[float, float] = (1, 1),
    ):
        validate_ladder_type(type_)
        super().__init__(group)
        image = pygame.image.load(type_).convert_alpha()
        scale = scale_ratio[0] * CELL_SIZE, scale_ratio[1] * CELL_SIZE
        self.image = pygame.transform.scale(image, (scale))
        self.rect = self.image.get_rect(
            topleft=convert_coordinate(coor, self.image.get_size())
        )
        self.head_rect = get_head_point(self.image, self.rect)
        self.tail_rect = get_tail_point(self.image, self.rect)
        self.take_pawns_coor = (
            Vector2(self.head_rect.topleft) - Vector2(self.tail_rect.topleft)
        ) // CELL_SIZE
        self.take_pawns_coor.x = int(self.take_pawns_coor.x)
        self.take_pawns_coor.y = int(self.take_pawns_coor.y)

    def update(self, display_surface: pygame.Surface):
        """Draw the head and tail points for debugging."""
        pygame.draw.rect(display_surface, "blue", self.head_rect, 5)
        pygame.draw.rect(display_surface, "green", self.tail_rect, 5)


def validate_ladder_type(type_: LadderType) -> None:
    ladder_types = [SMALL_BROWN_LADDER, SMALL_WHITE_LADDER, MID_LADDER, LARGE_LADDER]
    for ladder in ladder_types:
        if type_ not in ladder_types:
            raise ValueError(f"type doesnt matches to either of " + str(LadderType))
