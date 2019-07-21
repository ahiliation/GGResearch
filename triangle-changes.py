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
i=0

size = [800, 600]
screen = pygame.display.set_mode(size)

#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()


while not done:
  #  print i
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(10)
     
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
 

    while i < 100:
        pygame.draw.line(screen, GREEN, [i, i], [150,150], 5)
      #  time.sleep(0.1)
        pygame.draw.line(screen, RED, [150, 150], [150,300], 5)
      #  time.sleep(0.1)
        pygame.draw.line(screen, BLUE, [150, 300], [i, i], 5)
        pygame.display.flip()
        i = i + 1
        print i

    
pygame.quit()

