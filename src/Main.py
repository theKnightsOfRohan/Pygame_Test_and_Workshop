import pygame;
from Ball import Ball

pygame.init()

SCREEN_SIZE: tuple = (800, 600)

screen = pygame.display.set_mode(SCREEN_SIZE)

isRunning: bool = True

#Initialize a ball object
ball = Ball(400, 300, 50, (255, 0, 0))

while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

    screen.fill((0, 255, 0))
    ball.draw(screen)
    
    pygame.display.set_caption("Basic Sus")
    pygame.display.flip()
    pygame.display.update()