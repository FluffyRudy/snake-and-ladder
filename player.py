from settings import MAX_PAWNS, CELL_SIZE
import pygame
from pygame.sprite import Group
from pawn import PawnType, Pawn


class Player:
    def __init__(self, pawn_type: PawnType, offset: tuple[int, int], index: int):
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
        self.recent_rect = pygame.Rect(0, 0, CELL_SIZE, CELL_SIZE)
        self.player_index = index

    def draw(self, display_surface: pygame.Surface):
        self.group.draw(display_surface)

    def set_active_pawn(self, pawn: Pawn):
        self.active_pawn = pawn
        self.recent_rect = self.active_pawn.rect

    def get_active_pawn(self):
        return self.active_pawn
