import os
import time
import math 
import numpy
from sympy import symbols, exp, solve, Eq
from colorama import Fore, Back, Style 

#x = symbols('x')
y = symbols('y')
#p1, p2, p3 = Point(0, 0), Point(100, 100), Point(100, 100)


p1 = numpy.array((2,-3))
p2 = numpy.array((10,y))
expr1 = exp((10 - 2)**2 + (y - (-3))**2)

eq = Eq(expr1,100)
sol = solve(eq)

print(sol)





