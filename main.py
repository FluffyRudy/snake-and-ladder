import sys
import pygame
from settings import SCREEN_SIZE, BLACK


class Game:
    FPS = 60

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
        self.clock = pygame.time.Clock()

    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def run(self):
        while True:
            self.screen.fill(BLACK)
            self.handle_event()

            pygame.display.update()
            self.clock.tick(self.FPS)


def main():
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
