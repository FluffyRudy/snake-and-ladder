from settings import MAX_PAWNS, CELL_SIZE
import pygame
from pygame.sprite import Group
from pawn import PawnType, Pawn


class Player:
    def __init__(self, pawn_type: PawnType, offset: tuple[int, int]):
        self.group = Group()

        self.pawns = [
            Pawn(
                (offset[0], offset[1] + i * CELL_SIZE // 2),
                self.group,
                pawn_type,
            )
            for i in range(MAX_PAWNS)
        ]
        self.active_pawn = None

    def draw(self, display_surface: pygame.Surface):
        self.group.draw(display_surface)

    def move_pawn(value: int):
        pass

    def set_active_pawn(self, pawn: Pawn):
        self.active_pawn = pawn

    def get_active_pawn(self):
        return self.active_pawn
