import os
import time
import math 
import numpy
from sympy import symbols, exp, solve, Eq
from colorama import Fore, Back, Style 

#x = symbols('x')
x= symbols('x')
#p1, p2, p3 = Point(0, 0), Point(100, 100), Point(100, 100)


p1 = numpy.array((x,0))
p2 = numpy.array((2,-5))
p3 = numpy.array((-2,9))



expr1 = exp((2 - x)**2 + (-5 - 0)**2)
expr2 = exp((-2 -x)**2 + (9 - 0)**2)

eq = Eq(expr2,expr1)
sol = solve(eq)
print(sol)


#if ((p1p2 ==  p3p4) and (p2p3 == p4p1) and (p1p3 != p2p4) and (p1p2 != p2p3) and (p3p4 != p4p1)) :
#    print(Fore.BLACK, Back.WHITE + 'the given shape is a parallelogram')
#print(Style.DIM + 'and in dim text')
#    print(Style.RESET_ALL)



