import pygame
from pygame.math import Vector2
import math
from random import randrange
from path_util import join, iterate_files, GRAPHICS_DIRECTORY
from settings import (
    BOARD_POSITION,
    BOARD_SIZE,
    DICE_ANIMATION_SPEED,
    DICE_SPEED_DECREASE_FACTOR,
    CELL_SIZE,
)


class Dice:
    def __init__(self):
        self.rolled_value = 0

        self.frames = [
            pygame.image.load(file)
            for file in iterate_files(join(GRAPHICS_DIRECTORY, "dice_rotation"))
        ]
        self.dices = [
            pygame.transform.scale_by(pygame.image.load(file), (0.7, 0.7))
            for file in iterate_files(join(GRAPHICS_DIRECTORY, "dice"))
        ]

        self.image = self.frames[0]
        self.rect = self.image.get_rect(topleft=(400, 400))

        self.frame_index = 0
        self.roll_timer = 0
        self.roll_delay = 10

        self.do_roll = False
        self.is_selected = False

        self.direction = Vector2(0, 0)

        self.boundry = pygame.display.get_surface()

    def update(self):
        self.get_input()
        if self.do_roll:
            self.animate()
        self.roll_movements()

    def draw(self, display_surface: pygame.Surface):
        display_surface.blit(self.image, (self.rect.topleft))
        pygame.draw.rect(display_surface, "red", self.rect, 2, 5)

    def get_input(self):
        pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pos):
            self.is_selected = True
            self.start_pos = pos

        if not pygame.mouse.get_pressed()[0] and self.is_selected:
            dist, dir_ = self.calculate_vector(pos)
            drag_distance = math.hypot(
                self.start_pos[0] - pos[0], self.start_pos[1] - pos[1]
            )
            dice_size_average = (self.rect.width + self.rect.height) / 4
            if drag_distance > dice_size_average:
                self.start_rolling(pos)
            self.is_selected = False

    def start_rolling(self, pos):
        self.do_roll = True
        dist, dir_ = self.calculate_vector(pos)
        self.direction.x = dir_[0] * dist * 0.1
        self.direction.y = dir_[1] * dist * 0.1

    def animate(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.roll_timer >= self.roll_delay:
            self.roll_timer = current_time
            self.image = self.frames[int(self.frame_index)]
        self.frame_index += DICE_ANIMATION_SPEED
        if self.frame_index >= len(self.frames):
            self.frame_index = 0

    def stop_rolling(self):
        self.do_roll = False
        self.direction *= 0
        """ randrange: Exclusive, randint: Inclusive """
        value = randrange(1, 7)
        self.image = self.dices[value - 1]
        self.set_roll_value(value)

    def roll_movements(self):
        self.rect.x += self.direction.x * -1
        self.rect.y += self.direction.y * -1

        if self.direction.length() > 1:
            self.direction *= DICE_SPEED_DECREASE_FACTOR

        if self.do_roll and self.direction.length() < 1:
            self.stop_rolling()

        self.check_boundaries()

    def check_boundaries(self):
        if (
            self.rect.right + CELL_SIZE >= BOARD_POSITION[0] + BOARD_SIZE[0]
            or self.rect.left - CELL_SIZE < BOARD_POSITION[0]
        ):
            self.direction.x *= -1

        if (
            self.rect.top <= BOARD_POSITION[1] + CELL_SIZE
            or self.rect.bottom + CELL_SIZE >= BOARD_POSITION[1] + BOARD_SIZE[1]
        ):
            self.direction.y *= -1

    def calculate_vector(
        self, target_pos: tuple[int, int]
    ) -> tuple[float, tuple[float, float]]:
        distance = math.hypot(
            self.rect.left - target_pos[0], self.rect.top - target_pos[1]
        )
        direction = (self.rect.left - target_pos[0]) / (distance + 1), (
            self.rect.top - target_pos[1]
        ) / (distance + 1)
        return (distance, direction)

    def get_rolled_value(self):
        return self.rolled_value

    def set_roll_value(self, value: int):
        self.rolled_value = value
