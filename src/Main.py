import pygame, sys
from settings import *
from level import Level

from debug import debug

class Game: 
    def __init__(self):
        pygame.init()
        
        # initialize screen and clock
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("The Game")
        
        # initialize level
        self.level = Level()
        
    def run(self):
        while (True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Set the background color to gray
            self.screen.fill((100, 100, 100))
            # debug("FPS: " + str(self.clock.get_fps()))
            
            # run all of the logic in the level
            self.level.run()
            # update the screen
            pygame.display.update()
            # set the FPS
            self.clock.tick(FPS)
            
if (__name__ == "__main__"):
    # run the game
    game = Game()
    game.run()