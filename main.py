from settings import SCREEN_SIZE, BLACK, BOARD_POSITION, BOARD_SIZE
from path_util import join, GRAPHICS_DIRECTORY
import sys
import pygame
from game_manager import Manager
from windowui import WindowUI


class Game:
    FPS = 60

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
        self.clock = pygame.time.Clock()

        self.bg_image = pygame.transform.scale(
            pygame.image.load(join(GRAPHICS_DIRECTORY, "bg.png")).convert_alpha(),
            self.screen.get_size(),
        )
        self.game_manager = Manager(self.screen)
        self.windowui = WindowUI(self.screen)

    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def run(self):
        while True:
            self.screen.blit(self.bg_image, (0, 0))
            self.handle_event()

            if self.game_manager.get_winner() is None:
                self.game_manager.run()
            else:
                self.windowui.display_win_screen(self.game_manager.get_winner())

            pygame.display.update()
            self.clock.tick(self.FPS)


def main():
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
