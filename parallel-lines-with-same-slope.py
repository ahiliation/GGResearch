import os
import time
import random
from sympy import Point, Line
from sympy import symbols
from sympy.plotting import plot
from math import pi

 
# some code taken from https://www.geeksforgeeks.org/python-sympy-line-parallel_line-method/ 

x = symbols('x')
p1, p2, p3 = Point(0, 0), Point(100, 100), Point(100, 100)

l1 = Line(p1, p2)

p1 = plot(x*x, show=False)
p2 = plot(x, show=False)
p3 = plot(3*x, show=False)
p1.append(p2[0])


# using parallel_line() method
l2 = l1.parallel_line(p3)

# checking l2 is parallel to l1 using is_parallel() method
isParallel = l1.is_parallel(l2)

print(isParallel)
p3.show()