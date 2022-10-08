import os
import pygame
import time
from math import pi
from numpy import ones,vstack
from numpy.linalg import lstsq

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


#(y - y1)/(y2 - y1)
#(y - 3)/(1 - 3)
#N = (y - 3)
#D = (1 - 3)
#(x - x1)/(x2 - x1)
#N1 = (x - 2)
#D1 = (4 - 2)

#N/D = N1/D1
#N*D1 = D*N1

points = [(2,3),(4,1)]
x_coords, y_coords = zip(*points)
A = vstack([x_coords,ones(len(x_coords))]).T
m, c = lstsq(A, y_coords)[0]
print("Line Solution is y = {m}x + {c}".format(m=m,c=c))




while not done:
 
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(10)
     
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop



    y = 150
    x = 5.000000000000002 - y
    a = 4
    b = 5.000000000000002  - a
    pygame.draw.line(screen, WHITE, [a, b], [x, y], 1)    
    pygame.display.flip()


pygame.quit()

