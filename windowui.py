from settings import BLACK
from path_util import join, GRAPHICS_DIRECTORY, get_path
import pygame
from pygame.math import Vector2


class WindowUI:
    def __init__(self, display_surface: pygame.Surface):
        self.main_surface = display_surface
        self.game_win_screen = pygame.image.load(
            join(GRAPHICS_DIRECTORY, "win-screen.png")
        ).convert_alpha()
        self.pos = (
            Vector2(self.main_surface.get_size()) - self.game_win_screen.get_size()
        ) // 2

        font_path = get_path("fonts", "Topaz8-xxO8.ttf")
        self.font = pygame.font.Font(font_path, 50)

    def display_win_screen(self, winner: int):
        winner_text = self.font.render(f"PLAYER_{winner} WON", True, BLACK)
        self.main_surface.blit(self.game_win_screen, self.pos)
        self.main_surface.blit(
            winner_text,
            (
                (
                    self.pos.x
                    + self.game_win_screen.get_width()
                    - winner_text.get_width()
                )
                // 2,
                self.pos.y
                + self.game_win_screen.get_height() // 2
                + winner_text.get_height() * 2,
            ),
        )
