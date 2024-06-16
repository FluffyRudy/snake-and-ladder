from settings import (
    BLACK,
    BOARD_POSITION,
    BOARD_SIZE,
    NUM_CELLS,
    CELL_SIZE,
    PAWN_SIZE,
    update_alpha,
)
import pygame
from board import Board
from player import Player
from pawn import PawnType
from dice import Dice


class Manager:
    is_mouse_released = True

    def __init__(self, main_surface: pygame.Surface):
        self.main_surface = main_surface
        self.board = Board()
        self.bg_image = pygame.Surface((BOARD_SIZE), pygame.SRCALPHA)
        self.bg_image.fill(update_alpha(BLACK, 150))

        offset_0 = BOARD_POSITION[0] // 2, BOARD_POSITION[1] + 4 * PAWN_SIZE
        offset_1 = BOARD_POSITION[0] * 1.2 + BOARD_SIZE[0], offset_0[1]
        self.players = [
            Player(PawnType.RED, offset_0),
            Player(PawnType.GREEN, offset_1),
        ]
        self.num_players = len(self.players)
        self.turn = 0
        self.dice = Dice()

        self.finish_movement = True

        self.test_collide_rect = pygame.Rect(
            BOARD_POSITION[0] + CELL_SIZE * 5,
            BOARD_POSITION[1] + BOARD_SIZE[1] - CELL_SIZE,
            CELL_SIZE,
            CELL_SIZE,
        )

    def run(self):
        self.update()

        self.main_surface.blit(self.bg_image, BOARD_POSITION)
        self.board.draw_grid(self.main_surface)
        self.draw()

    def draw(self):
        for player in self.players:
            player.draw(self.main_surface)
        self.dice.draw(self.main_surface)
        pygame.draw.rect(self.main_surface, "red", self.test_collide_rect, 2)

    def update(self):
        self.handle_event()
        self.player_movement()

    def handle_event(self):
        mouse_pos = pygame.mouse.get_pos()

        if (
            pygame.mouse.get_pressed()[0]
            and self.finish_movement
            and self.dice.get_rolled_value() != 0
        ):
            for pawn in self.current_player().pawns:
                if pawn.rect.collidepoint(mouse_pos) and self.is_mouse_released:
                    self.is_mouse_released = False
                    self.finish_movement = False
                    self.current_player().set_active_pawn(pawn)
                    self.get_active_pawn().set_roll_value(self.dice.get_rolled_value())
                    self.dice.set_roll_value(0)
                    break

        if not pygame.mouse.get_pressed()[0]:
            self.is_mouse_released = True

    def player_movement(self):
        if (
            not self.finish_movement
            and not self.players[self.turn].get_active_pawn() is None
        ):
            self.get_active_pawn().move()
            if self.get_active_pawn().has_movement_end():
                self.finish_movement = True
                self.switch_turn()

    def current_player(self) -> Player:
        return self.players[self.turn]

    def get_active_pawn(self):
        return self.current_player().get_active_pawn()

    def custom_movement(self, x, y):
        pass

    def switch_turn(self):
        self.turn = (self.turn + 1) % self.num_players

    def allow_dice_movement(self):
        pass
