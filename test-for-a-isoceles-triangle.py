import os
import time
from math import pi
import numpy

 

#x = symbols('x')
#p1, p2, p3 = Point(0, 0), Point(100, 100), Point(100, 100)

#stackoveflow

p1 = numpy.array((5,-2))
p2 = numpy.array((6,4))
p3 = numpy.array((7,-2))
p1p2 = numpy.linalg.norm(p1-p2)
p2p3 = numpy.linalg.norm(p2-p3)
p3p1 = numpy.linalg.norm(p3-p1)

print("p1p2 =",p1p2)
print("p2p3 =", p2p3)
print("p1p3 =", p3p1)

if ((p1p2 ==  p2p3) or (p1p2 == p3p1)):
    print("This is an Isoceles triangle\n")
else:
    print("No Isoceles triangle \n")



