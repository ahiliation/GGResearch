import os
import time
import math 
import numpy
from sympy.solvers import solve
from sympy import Symbol, simplify
from sympy import exp, Eq
from colorama import Fore, Back, Style 

#x = symbols('x')
x= Symbol('x')
y= Symbol('y')
#p1, p2, p3 = Point(0, 0), Point(100, 100), Point(100, 100)


expr1 = exp((x - 3)**2 + (y - 6)**2)
expr2 = exp((x + 3)**2 + (y - 4)**2)

#print(expr2)
eq = Eq(expr2 - expr1,0)
#sol = solve(eq)
smpl = simplify(eq)
print("After Simplification : {}".format(smpl)) 




