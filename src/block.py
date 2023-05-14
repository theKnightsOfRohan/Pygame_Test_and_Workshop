import pygame
from settings import *

class Block(pygame.sprite.Sprite):
    def __init__(self, pos, tile_type):
        super().__init__(tile_type)
        # Get the drawbox of the sprite
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill((0, 0, 0))
        # self.image = pygame.image.load("../assets/tile.png").convert_alpha()
        # Set the position of the sprite's drawbox
        self.rect = self.image.get_rect(topleft = pos)