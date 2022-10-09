import os
import pygame
import time
import random
from sympy import Point, Line

from math import pi

pygame.init()

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)


size = [640, 480]
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
 
# some code taken from https://www.geeksforgeeks.org/python-sympy-line-parallel_line-method/ 

    p1, p2, p3 = Point(0, 0), Point(100, 100), Point(200, 300)

    l1 = Line(p1, p2)

    # using parallel_line() method
    l2 = l1.parallel_line(p3)

# checking l2 is parallel to l1 using is_parallel() method
    isParallel = l1.is_parallel(l2)

    print(isParallel)
    l2.ambient_dimension
    pygame.display.flip()


pygame.quit()

