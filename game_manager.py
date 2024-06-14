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
        self.dice = Dice()

    def run(self):
        self.main_surface.blit(self.bg_image, BOARD_POSITION)
        self.board.draw_grid(self.main_surface)
        self.draw()

    def draw(self):
        for player in self.players:
            player.draw(self.main_surface)
        self.dice.draw(self.main_surface)

    def update(self):
        pass
