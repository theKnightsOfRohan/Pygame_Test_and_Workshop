import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, tile_type, obstacle_sprites):
        super().__init__(tile_type)
        # Get the drawbox of the sprite
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill((255, 255, 255))
        # self.image = pygame.image.load("../assets/player.png").convert_alpha()
        # Set the position of the sprite's drawbox
        self.rect = self.image.get_rect(topleft = pos)
        
        # Set the initial movement vector to 0
        self.direction = pygame.math.Vector2(0, 0)
        # Set the speed of the player as it moves fluidly on screen
        self.speed = 5
        
        # Get all of the possible collsion sprites
        self.obstacle_sprites = obstacle_sprites

    def input(self):
        # Get the keys that are pressed and adjust movement vector accordingly
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_UP]):
            self.direction.y = -1
        elif (keys[pygame.K_DOWN]):
            self.direction.y = 1
        else:
            self.direction.y = 0
            
        if (keys[pygame.K_LEFT]):
            self.direction.x = -1
        elif (keys[pygame.K_RIGHT]):
            self.direction.x = 1
        else:
            self.direction.x = 0
            
    def move(self, speed):
        # Normalize the direction vector to prevent faster diagonal movement
        if (self.direction.magnitude() != 0):
            self.direction = self.direction.normalize()
        
        # Move the player in the direction of the movement vector
        # Then check for collisions for that direction
        self.rect.x += self.direction.x * speed
        self.collision('horizontal')
        
        self.rect.y += self.direction.y * speed
        self.collision('vertical')
        
    def collision(self, direction):
        # Check for vertical and horizontal collisions via the collision rectangle/sprite overlap
        # If there is a collision, move the player back to the edge of the object
        # Determine direction based on the direction at the moment of collision
        if (direction == 'horizontal'):
            for (sprite) in (self.obstacle_sprites):
                if (sprite.rect.colliderect(self.rect)):
                    if (self.direction.x > 0):
                        self.rect.right = sprite.rect.left
                    elif (self.direction.x < 0):
                        self.rect.left = sprite.rect.right
                    break
      
        if (direction == 'vertical'):
            for (sprite) in (self.obstacle_sprites):
                if (sprite.rect.colliderect(self.rect)):
                    if (self.direction.y > 0):
                        self.rect.bottom = sprite.rect.top
                    elif (self.direction.y < 0):
                        self.rect.top = sprite.rect.bottom
                    break
    
    def update(self):
        self.input()
        self.move(self.speed)