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


size = [800, 600]
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
 

    for i in range(450):
        pygame.draw.polygon(screen, WHITE, [[100, 100], [0, 200], [200, 200]], 5) # typical triangle related
        pygame.draw.polygon(screen, WHITE, [[100, 100], [i, 200], [200, i]], 5)
        pygame.draw.polygon(screen, WHITE, [[i, i], [i, i], [i, i]], 5) # straight line related
        pygame.display.flip()

    
pygame.quit()

