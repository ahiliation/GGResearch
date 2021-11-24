import os
import pygame
import time
import random
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


#blockSize = 20 #Set the size of the grid block
#for x in range(0, 800, blockSize):
#    for y in range(0, 600, blockSize):
#        rect = pygame.Rect(x, y, blockSize, blockSize)
#        pygame.draw.rect(screen, WHITE, rect, 1)




while not done:
 
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(10)
     
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop




    m = 100
    while True:
        c = 10
        x = random.randint(1,800)
        y = random.randint(1,600)
        y1 = m*x + c
        x1 = (y - c)/m
        print(x,y)
        print(x1,y1)
        # if y < 600:
        pygame.draw.line(screen, BLUE, [x1, y1], [x,y], 1)
        time.sleep(0.01)
        pygame.display.flip()
       

pygame.quit()

