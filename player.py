from typing import Optional
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

        self.rolled_value: int = 0
        self.move_made = False
        self.key_released = True

    def draw(self, display_surface: pygame.Surface):
        self.group.draw(display_surface)

    def update(self, value: int, snake_group: Group):
        value = 29
        if self.rolled_value == 0 and value is not None:
            self.rolled_value = value
            self.move_made = True
        pos = pygame.mouse.get_pos()

        if (
            pygame.mouse.get_pressed()[0]
            and self.key_released
            and not self.rolled_value is None
        ):
            for idx, pawn in enumerate(self.pawns):
                if pawn.rect.collidepoint(pos):
                    self.active_pawn = pawn
                    self.key_released = False

        if self.rolled_value > 0 and isinstance(self.active_pawn, Pawn):
            future_x, future_y = self.active_pawn.calculate_future_position(
                self.rolled_value
            )
            future_rect = pygame.Rect(future_x, future_y, CELL_SIZE, CELL_SIZE)
            self.active_pawn.move()
        elif not self.active_pawn is None and self.rolled_value <= 0:
            self.halt_pawn()

        if self.rolled_value > 0 and not (self.active_pawn is None):
            self.rolled_value -= 1

        if not pygame.mouse.get_pressed()[0]:
            self.key_released = True
        return self.rolled_value == 0 and self.move_made

    def halt_pawn(self):
        self.active_pawn = None
        self.rolled_value = 0
        self.is_turn = False
        self.will_collide = False
