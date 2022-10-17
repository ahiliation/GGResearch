import os
import time
from math import pi
import numpy

 
# some code taken from https://www.geeksforgeeks.org/python-sympy-line-parallel_line-method/ 

#x = symbols('x')
#p1, p2, p3 = Point(0, 0), Point(100, 100), Point(100, 100)

#stackoveflow

p1 = numpy.array((0,0))
p2 = numpy.array((36,15))
distance = numpy.linalg.norm(p1-p2)

print(distance)

#l1 = Line(p1, p2)

#p1 = plot(x, show=False)
#p2 = plot(-x +5, show=False)
##p3 = plot(x +10, show=False)
#p1.append(p2[0])

#p1.show()

