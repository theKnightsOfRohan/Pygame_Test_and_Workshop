import pygame, sys
from settings import *
from level import Level

from debug import debug

class Game: 
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("The Game")
        
        self.level = Level()
        
    def run(self):
        while (True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill((100, 100, 100))
            # debug("FPS: " + str(self.clock.get_fps()))
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)
            
if (__name__ == "__main__"):
    game = Game()
    game.run()