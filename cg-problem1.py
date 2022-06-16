import os
import pygame
import time
from math import pi

pygame.init()

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)


size = [800,600]
screen = pygame.display.set_mode(size)

#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()


while not done:
 
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(10)
     
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
 

    for y in range(400):
        pygame.draw.aaline(screen, GREEN, [10, 200], [200,y], 1)
        time.sleep(0.01)
        pygame.display.flip()
    for x in range(200, -1, -1):
        pygame.draw.aaline(screen, RED, [10, 200], [x,400], 1)
        time.sleep(0.01)
        if x == 10:
            break
        pygame.display.flip()


pygame.quit()

