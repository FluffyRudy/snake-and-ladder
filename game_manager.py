from settings import (
    BLACK,
    BOARD_POSITION,
    BOARD_SIZE,
    NUM_CELLS,
    CELL_SIZE,
    PAWN_SIZE,
    SNAKE_COORS,
    SNAKE_SCALES,
    PAWN_DOWN_LEN,
    update_alpha,
)
from typing import Optional
from path_util import join, iterate_files, GRAPHICS_DIRECTORY
import pygame
from board import Board
from player import Player
from pawn import PawnType
from dice import Dice
from snake import Snake


class Manager:
    def __init__(self, main_surface: pygame.Surface):
        self.main_surface = main_surface
        self.board = Board()
        self.bg_image = pygame.Surface((BOARD_SIZE), pygame.SRCALPHA)
        self.bg_image.fill(update_alpha(BLACK, 255))

        offset_0 = BOARD_POSITION[0] // 2, BOARD_POSITION[1] + 4 * PAWN_SIZE
        offset_1 = BOARD_POSITION[0] * 1.2 + BOARD_SIZE[0], offset_0[1]
        self.players = [
            Player(PawnType.RED, offset_0),
            Player(PawnType.GREEN, offset_1),
        ]
        self.num_players = len(self.players)
        self.turn = 0

        self.dice = Dice()

        # snakes
        self.snake_group = pygame.sprite.Group()
        snake_images = iterate_files(join(GRAPHICS_DIRECTORY, "snake"))[:3]

        for index, path in enumerate(snake_images):
            Snake(
                SNAKE_COORS[index][:3],
                path,
                self.snake_group,
                PAWN_DOWN_LEN[index],
                SNAKE_SCALES[index],
            )

    def run(self):
        self.update()
        self.main_surface.blit(self.bg_image, BOARD_POSITION)
        self.board.draw_grid(self.main_surface)
        self.draw()

    def draw(self):
        self.highlight_active_pawns()
        for player in self.players:
            player.draw(self.main_surface)
        self.snake_group.draw(self.main_surface)
        self.dice.draw(self.main_surface)
        for snake in self.snake_group:
            pygame.draw.rect(self.main_surface, "red", snake.collide_rect, 2)

    def update(self):
        if self.players[self.turn].rolled_value == 0:
            self.dice.update()
        value = self.dice.get_rolled_value()
        done_roll = self.players[self.turn].update(value, self.snake_group)
        if done_roll:
            self.players[self.turn].move_made = False
            self.turn = (self.turn + 1) % self.num_players
        pygame.draw.rect(
            self.main_surface, "red", (BOARD_POSITION, (CELL_SIZE, CELL_SIZE)), 5, 5
        )

    def highlight_active_pawns(self):
        for pawn in self.players[self.turn].pawns:
            pygame.draw.circle(
                self.main_surface, "white", pawn.rect.center, PAWN_SIZE // 2 + 5, 5
            )

    def check_collision(self, value: Optional[int]):
        if value is None:
            return False
