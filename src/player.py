import pygame
from settings import *
from spritesheet import SpriteSheet

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, tile_type, obstacle_sprites):
        super().__init__(tile_type)
        # Get the spritesheet and drawbox of the sprite
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.spritesheet = SpriteSheet("assets/Boy/SpriteSheet.png")
        self.image = self.spritesheet.image_at((0, 0, 16, 16)).convert_alpha()
        self.image = pygame.transform.scale(self.image, (TILESIZE, TILESIZE))
        # Set the position of the sprite's drawbox
        self.rect = self.image.get_rect(topleft = pos)
        # Set the hitbox of the sprite to be slightly smaller in the Y direction 
        # allows for sprite stacking for the illusion of depth
        self.hitbox = self.rect.inflate(0, -26)
        
        # Set the initial movement vector to 0
        self.direction = pygame.math.Vector2(0, 0)
        # Set the speed of the player as it moves fluidly on screen
        self.speed = 5
        
        # Get all of the possible collision sprites
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
        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')
        
        self.rect.center = self.hitbox.center
        
    def collision(self, direction):
        # Check for vertical and horizontal collisions via hitbox collision
        # If there is a collision, move the player back to the edge of the object
        # Determine direction based on the direction at the moment of collision
        if (direction == 'horizontal'):
            for (sprite) in (self.obstacle_sprites):
                if (sprite.hitbox.colliderect(self.hitbox)):
                    if (self.direction.x > 0):
                        self.hitbox.right = sprite.hitbox.left
                    elif (self.direction.x < 0):
                        self.hitbox.left = sprite.hitbox.right
                    break
      
        if (direction == 'vertical'):
            for (sprite) in (self.obstacle_sprites):
                if (sprite.hitbox.colliderect(self.hitbox)):
                    if (self.direction.y > 0):
                        self.hitbox.bottom = sprite.hitbox.top
                    elif (self.direction.y < 0):
                        self.hitbox.top = sprite.hitbox.bottom
                    break
    
    def update(self):
        self.input()
        self.move(self.speed)