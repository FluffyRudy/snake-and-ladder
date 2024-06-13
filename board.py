from settings import (
    BOARD_SIZE,
    BOARD_POSITION,
    NUM_CELLS,
    CELL_SIZE,
    WHITE,
    BLACK,
    update_alpha,
)
import pygame


class Board:
    def __init__(self):
        self.surface = pygame.Surface(BOARD_SIZE, pygame.SRCALPHA)
        self.surface.fill(update_alpha(WHITE, 150))

    def draw(self, main_surface: pygame.Surface):
        self.draw_grids()
        main_surface.blit(self.surface, (BOARD_POSITION))

    def draw_grids(self):
        for y in range(NUM_CELLS):
            for x in range(NUM_CELLS):
                pos_x = x * CELL_SIZE
                pos_y = y * CELL_SIZE
                pygame.draw.rect(
                    self.surface, BLACK, (pos_x, pos_y, CELL_SIZE, CELL_SIZE), 3, 5
                )
