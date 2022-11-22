import os
import time
import math 
import numpy
from sympy.solvers import solve
from sympy import Symbol
from sympy import exp, Eq
from colorama import Fore, Back, Style 

#x = symbols('x')
x= Symbol('x')
#p1, p2, p3 = Point(0, 0), Point(100, 100), Point(100, 100)


p = numpy.array((5,-3))
q = numpy.array((0,1))
r = numpy.array((-x,6))



expr1 = exp((5 - 0)**2 + (-3 - 1)**2)
expr2 = exp((0 - x)**2 + (1 - 6)**2)

eq = Eq(expr2 - expr1,0)
sol = solve(eq)
print(sol)
r1 = numpy.array((4,6))
r2 = numpy.array((-4,6))
distance1 = numpy.linalg.norm(p-r1)
print("distance pr =", distance1)
distance2 = numpy.linalg.norm(q-r2)
print("distance qr =", distance2)





