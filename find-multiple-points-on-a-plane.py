import os
import time
import math 
import numpy
from sympy import Symbol, var
from sympy.solvers import solve, solveset, S
from sympy import  exp, Eq
from colorama import Fore, Back, Style 

#x = symbols('x')
y = Symbol('y')
#y = var('y', real=True)
#p1, p2, p3 = Point(0, 0), Point(100, 100), Point(100, 100)


p1 = numpy.array((2,-3))
p2 = numpy.array((10,y))
expr1 = exp((10 - 2)**2 + (y - (-3))**2)

#print(expr1)

eq = Eq(expr1 - 100,0)
#print(eq)

sol = solveset(eq, y, domain=S.Complexes)

print(sol)





