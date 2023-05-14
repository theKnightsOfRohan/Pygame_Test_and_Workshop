import pygame
from settings import *
from block import Block
from player import Player

from debug import debug

class Level:
    def __init__(self):
        # access screen without using it as an argument
        self.display_surface = pygame.display.get_surface()
        
        # Sprite group setup:
        # - Visibile sprites are those that are rendered
        # - Obstacle sprites are those that the player can collide with (NOT including the player)
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()
        
        self.create_map()
        
    def create_map(self):
        # create map from MAP 2d array in settings.py
        
        for (row_index, row) in enumerate(MAP):
            print(str(row_index) + ": " + str(row))
            for (col_index, col) in enumerate(row):
                # get screen coordinates from tile coordinates
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                
                # create object on map based on tile type
                if (col == "w"):
                    Block((x, y), [self.visible_sprites, self.obstacle_sprites])
                elif col == "p":
                    self.player = Player((x, y), [self.visible_sprites], self.obstacle_sprites)
        
    def run(self):
        # update and draw sprites
        self.visible_sprites.update()
        self.visible_sprites.draw(self.display_surface)
        debug(self.player.direction)