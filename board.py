from settings import (
    BOARD_SIZE,
    BOARD_POSITION,
    NUM_CELLS,
    CELL_SIZE,
    WHITE,
    BLACK,
    BOARDER_RADIUS,
    BORDER_WIDTH,
    update_alpha,
    random_rgb_color,
    normalized_color,
)
import pygame


class Board:
    def __init__(self):
        self.font = pygame.font.Font("fonts/Topaz8-xxO8.ttf", 25)

    def draw_grid(self, surface: pygame.Surface):
        count = 100
        for y in range(NUM_CELLS):
            for x in range(NUM_CELLS):
                posx = BOARD_POSITION[0] + x * CELL_SIZE
                posy = BOARD_POSITION[1] + y * CELL_SIZE
                border_radius = self.__get_border_radius(x, y)
                self.__draw_cell(surface, (posx, posy), **border_radius)
                _count = (count - x) if y % 2 == 0 else (count - NUM_CELLS + x + 1)
                text = self.font.render(str(_count), True, WHITE)
                surface.blit(
                    text,
                    (
                        posx + CELL_SIZE // 2 - text.get_width() // 2,
                        posy + CELL_SIZE // 2 - text.get_height() // 2,
                    ),
                )
                pygame.draw.circle(
                    surface,
                    normalized_color(x, NUM_CELLS),
                    (posx + CELL_SIZE // 2, posy + CELL_SIZE // 2),
                    CELL_SIZE // 2 - 2,
                    BORDER_WIDTH + 2,
                )
            count -= NUM_CELLS

    def __draw_cell(
        self,
        display_surface: pygame.Surface,
        pos: tuple[int, int],
        **border_radius,
    ):
        pygame.draw.rect(
            display_surface,
            WHITE,
            (pos, (CELL_SIZE, CELL_SIZE)),
            BORDER_WIDTH,
            border_top_left_radius=border_radius.get("tl", 0),
            border_bottom_left_radius=border_radius.get("bl", 0),
            border_top_right_radius=border_radius.get("tr", 0),
            border_bottom_right_radius=border_radius.get("br", 0),
        )

    def __get_border_radius(self, x, y):
        radius = {"tl": 0, "bl": 0, "tr": 0, "br": 0}
        if x == 0 and y == 0:
            radius["tl"] = BOARDER_RADIUS
        if x == 0 and y == NUM_CELLS - 1:
            radius["bl"] = BOARDER_RADIUS
        if x == NUM_CELLS - 1 and y == 0:
            radius["tr"] = BOARDER_RADIUS
        if x == NUM_CELLS - 1 and y == NUM_CELLS - 1:
            radius["br"] = BOARDER_RADIUS
        return radius

    def get_cell_index_by(self, pos: tuple[int, int]):
        pass
