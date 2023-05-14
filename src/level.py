import pygame
from settings import *

class Level:
    def __init__(self):
        # access screen without using it as an argument
        self.display_surface = pygame.display.get_surface()
        
        # Sprite group setup
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()
        
        self.create_map()
        
    def create_map(self):
        for (row_index, row) in enumerate(MAP):
            print(str(row_index) + ": " + str(row))
            for col in row:
                if col == "1":
                    pass
                    # self.obstacle_sprites.add(Tile())
                elif col == "P":
                    pass
                    # self.visible_sprites.add(Player())
        
    def run(self):
        # update and draw sprites
        pass