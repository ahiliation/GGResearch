import os
import time
import math 
import numpy
import sympy as sp
from sympy.solvers import solve
from sympy import symbols, simplify
from sympy import exp, Eq
from colorama import Fore, Back, Style 

x,y = sp.symbols('x y')



expr1 = (x - 3)**2 + (y - 6)**2
expr2 = (x + 3)**2 + (y - 4)**2
sim = sp.ratsimp(expr2 - expr1)

print(sp.simplify(sim))
eq = Eq(expr2 - expr1,0)
#sol = solve(eq)
smpl = sp.simplify(eq)
print("After Simplification : {}".format(smpl)) 




