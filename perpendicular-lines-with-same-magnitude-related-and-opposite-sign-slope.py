import os
import time
from sympy import Point, Line
from sympy import symbols
from sympy.plotting import plot
from math import pi

 
# some code taken from https://www.geeksforgeeks.org/python-sympy-line-parallel_line-method/ 

x = symbols('x')
p1, p2, p3 = Point(0, 0), Point(100, 100), Point(100, 100)

l1 = Line(p1, p2)

p1 = plot(x, show=False)
p2 = plot(-x +5, show=False)
#p3 = plot(x +10, show=False)
p1.append(p2[0])

p1.show()

