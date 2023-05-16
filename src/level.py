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
        self.visible_sprites = YSortCameraGroup()
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
        self.visible_sprites.custom_draw(self.player)
        debug(self.player.direction)
        
class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        # get screen dimensions
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_width()/2
        self.half_height = self.display_surface.get_height()/2
        
        #Declares the offset vector (initial values are unimportant)
        self.offset = pygame.math.Vector2(0, 0)
        
    def custom_draw(self, player):
        # update offset based on player position
        # offset centers player on the screen
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height
        
        # draw sprites in order, based on y position
        # offset_pos is the position of the sprite on the screen
        # lambda function is used to sort sprites based on y position
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)
            