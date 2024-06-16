from typing import Literal
from settings import CELL_SIZE, BOARD_POSITION, BOARD_SIZE, PAWN_SIZE, RED
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
        groups: Group,
        type_: PawnType,
    ):
        super().__init__(groups)

        self.image = pygame.image.load(Pawn.get_pawn(type_))
        self.rect = self.image.get_rect(topleft=pos)
        self.type_ = type_
        self.roll_value = 0
        self.c_move = Vector2(0, 0)
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
        if self.roll_value != 0:
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
            self.roll_value = max(self.roll_value - 1, 0)

        if int(self.c_move.x) != 0:
            if self.c_move.x > 0:
                self.rect.x += CELL_SIZE
                self.c_move.x -= 1
            elif self.c_move.x < 0:
                self.rect.x -= CELL_SIZE
                self.c_move.x += 1
        if int(self.c_move.y) != 0:
            if self.c_move.y > 0:
                self.rect.y += CELL_SIZE
                self.c_move.y -= 1
            elif self.c_move.y < 0:
                self.rect.y -= CELL_SIZE
                self.c_move.y += 1
        print(self.c_move)
        time.sleep(0.1)

    def set_cmove(self, x: int, y: int):
        self.c_move.x = int(x)
        self.c_move.y = int(y)

    def has_movement_end(self):
        return (
            self.roll_value == 0 and int(self.c_move.x) == 0 and int(self.c_move.y) == 0
        )

    def set_roll_value(self, value: int):
        self.roll_value = value
