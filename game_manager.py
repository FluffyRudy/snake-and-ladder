from settings import (
    BLACK,
    BOARD_POSITION,
    BOARD_SIZE,
    NUM_CELLS,
    CELL_SIZE,
    update_alpha,
)
import pygame
from board import Board


class Manager:
    def __init__(self, main_surface: pygame.Surface):
        self.main_surface = main_surface
        self.board = Board()
        self.bg_image = pygame.Surface((BOARD_SIZE), pygame.SRCALPHA)
        self.bg_image.fill(update_alpha(BLACK, 150))

    def run(self):
        self.main_surface.blit(self.bg_image, BOARD_POSITION)
        self.board.draw_grid(self.main_surface)
