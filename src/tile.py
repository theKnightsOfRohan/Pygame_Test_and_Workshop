import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, tile_type):
        super().__init__(tile_type)
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill((255, 255, 255))
        # self.image = pygame.image.load("../assets/tile.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)