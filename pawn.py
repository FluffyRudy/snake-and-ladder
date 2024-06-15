from typing import Literal
from settings import BOARD_POSITION, PAWN_SIZE, BOARD_SIZE, CELL_SIZE, RED
from path_util import join, GRAPHICS_DIRECTORY
from enum import Enum
import pygame
from pygame.math import Vector2
from pygame.sprite import Sprite, Group
import time


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

        self.image = pygame.transform.scale(
            pygame.image.load(Pawn.get_pawn(type_)), (PAWN_SIZE, PAWN_SIZE)
        )
        self.rect = self.image.get_rect(topleft=pos)

        self.onboard = False
        self.direction = 1

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

    def move(self):
        if not self.onboard:
            self.rect.centerx = BOARD_POSITION[0] + CELL_SIZE // 2
            self.rect.y = (
                BOARD_POSITION[1] + BOARD_SIZE[1] - (CELL_SIZE + PAWN_SIZE) // 2
            )
            self.onboard = True
        else:
            new_dist = self.rect.x + self.direction * CELL_SIZE
            if new_dist > (BOARD_POSITION[0] + BOARD_SIZE[0]):
                self.rect.y -= CELL_SIZE
                new_dist = self.rect.x - CELL_SIZE
                self.direction = -1
            elif new_dist < BOARD_POSITION[0]:
                self.rect.y -= CELL_SIZE
                new_dist = self.rect.x + CELL_SIZE
                self.direction = 1
            else:
                self.rect.x = new_dist
                time.sleep(0.1)
