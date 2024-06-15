import pygame
from pygame.sprite import Group, Sprite
from settings import CELL_SIZE, BOARD_POSITION


class Snake(Sprite):
    def __init__(
        self,
        pos: tuple[int, int],
        image: str,
        group: Group,
        down_to: tuple[int, int],
        scale: tuple[int, int] = (1, 1),
    ):
        super().__init__(group)
        self.image = pygame.transform.scale_by(pygame.image.load(image), scale)
        self.rect = self.image.get_rect(topleft=pos)
        self.collide_rect = pygame.Rect(*self.rect.topleft, *(CELL_SIZE, CELL_SIZE))
        self.down_to = down_to
