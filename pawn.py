from typing import Literal
from settings import CELL_SIZE, RED
from path_util import join, GRAPHICS_DIRECTORY
from enum import Enum
import pygame
from pygame.math import Vector2
from pygame.sprite import Sprite, Group


class PawnType(Enum):
    GREEN = 0
    YELLOW = 1
    RED = 2
    BLUE = 3


class Pawn(Sprite):
    def __init__(
        self,
        pos: tuple[int, int],
        groups: list[Group],
        type_: PawnType,
    ):
        super().__init__(groups)

        self.image = pygame.image.load(Pawn.get_pawn(type_))
        self.rect = self.image.get_rect(topleft=pos)

    @classmethod
    def get_pawn(self, type_: PawnType) -> str:
        base_dir = join(GRAPHICS_DIRECTORY, "pawn")
        pawn_map = {
            PawnType.RED: join(base_dir, "red.png"),
            PawnType.BLUE: join(base_dir, "blue.png"),
            PawnType.YELLOW: join(base_dir, "yellow.png"),
            PawnType.GREEN: join(base_dir, "green.png"),
        }
        return pawn_map.get(type_)
