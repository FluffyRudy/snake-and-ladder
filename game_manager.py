from settings import (
    BLACK,
    BOARD_POSITION,
    BOARD_SIZE,
    NUM_CELLS,
    CELL_SIZE,
    PAWN_SIZE,
    LARGE_LADDER,
    SMALL_WHITE_LADDER,
    SMALL_BROWN_LADDER,
    MID_LADDER,
    update_alpha,
)
from typing import Optional
import time
from random import randrange
import pygame
from pygame.sprite import Group
from board import Board
from player import Player
from pawn import Pawn, PawnType
from dice import Dice
from snake import Snake
from ladder import Ladder


class Manager:
    is_mouse_released = True
    MIN_SNAKE_DISTANCE = 2 * CELL_SIZE

    def __init__(self, main_surface: pygame.Surface):
        self.main_surface = main_surface
        self.board = Board()
        self.bg_image = pygame.Surface(BOARD_SIZE, pygame.SRCALPHA)
        self.bg_image.fill(update_alpha(BLACK, 150))

        offset_0 = BOARD_POSITION[0] // 2, BOARD_POSITION[1] + 4 * PAWN_SIZE
        offset_1 = BOARD_POSITION[0] * 1.2 + BOARD_SIZE[0], offset_0[1]
        self.players = [
            Player(PawnType.RED, offset_0),
            Player(PawnType.GREEN, offset_1),
        ]
        self.num_players = len(self.players)
        self.turn = 0

        self.snake_group = Group()
        for _ in range(3):
            self.place_snake()
        self.sort_snakes()

        self.ladder_group = Group()
        self.place_ladders()

        self.dice = Dice()
        self.finish_movement = True

    def run(self):
        self.update()
        self.main_surface.blit(self.bg_image, BOARD_POSITION)
        self.board.draw_grid(self.main_surface)
        self.draw()

    def draw(self):

        self.snake_group.draw(self.main_surface)
        self.snake_group.update(self.main_surface)
        self.ladder_group.update(self.main_surface)
        self.ladder_group.draw(self.main_surface)
        for player in self.players:
            player.draw(self.main_surface)
        self.dice.draw(self.main_surface)

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
                snake_collision_cmove = self.pawn_snake_collision(
                    self.get_active_pawn()
                )
                ladder_collision_cmove = self.pawn_ladder_collision(
                    self.get_active_pawn()
                )
                if not snake_collision_cmove is None:
                    self.get_active_pawn().set_cmove(*snake_collision_cmove)
                elif not ladder_collision_cmove is None:
                    self.get_active_pawn().reverse_direction()
                    self.get_active_pawn().set_cmove(*ladder_collision_cmove)
                else:
                    self.finish_movement = True
                    if self.get_active_pawn().get_cnst_roll_value() != 6:
                        self.switch_turn()

    def current_player(self) -> Player:
        return self.players[self.turn]

    def get_active_pawn(self):
        return self.current_player().get_active_pawn()

    def custom_movement(self, x, y):
        pass

    def switch_turn(self):
        self.get_active_pawn().reset_cnst_roll_value()
        self.turn = (self.turn + 1) % self.num_players

    def is_valid_snake_position(self, pos: tuple[int, int]):
        for snake in self.snake_group:
            distance = (
                (snake.rect.x - pos[0]) ** 2 + (snake.rect.y - pos[1]) ** 2
            ) ** 0.5
            if distance < self.MIN_SNAKE_DISTANCE:
                return False
        return True

    def pawn_snake_collision(self, pawn: Pawn) -> Optional[tuple[int, int]]:
        for snake in self.snake_group:
            if pawn.rect.colliderect(snake.head_rect):
                return snake.throw_pawns_coor
        return None

    def pawn_ladder_collision(self, pawn: Pawn) -> Optional[tuple[int, int]]:
        for ladder in self.ladder_group:
            if pawn.rect.colliderect(ladder.tail_rect):
                return ladder.take_pawns_coor
        return None

    def place_snake(self):
        max_x = BOARD_POSITION[0] + BOARD_SIZE[0] - CELL_SIZE
        max_y = BOARD_POSITION[1] + BOARD_SIZE[1] - CELL_SIZE
        while True:
            random_pos = (
                randrange(BOARD_POSITION[0], max_x, CELL_SIZE),
                randrange(BOARD_POSITION[1], max_y, CELL_SIZE),
            )
            if self.is_valid_snake_position(random_pos):
                break
        Snake(random_pos, self.snake_group)

    def sort_snakes(self):
        sorted_snakes = sorted(self.snake_group, key=lambda snake: snake.rect.y)
        self.snake_group.empty()
        for snake in sorted_snakes:
            self.snake_group.add(snake)

    def place_ladders(self):
        Ladder((0, -2), self.ladder_group, LARGE_LADDER, scale_ratio=(1, 6.5))
        Ladder((5, -6), self.ladder_group, MID_LADDER, scale_ratio=(1, 2.5))
        Ladder((8.1, 0), self.ladder_group, SMALL_WHITE_LADDER, scale_ratio=(0.8, 3.5))
