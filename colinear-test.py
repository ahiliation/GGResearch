import os
import time
from math import pi
import numpy

 

#x = symbols('x')
#p1, p2, p3 = Point(0, 0), Point(100, 100), Point(100, 100)

#stackoveflow

p1 = numpy.array((1,5))
p2 = numpy.array((2,3))
p3 = numpy.array((-2,-11))
p1p2 = numpy.linalg.norm(p1-p2)
p2p3 = numpy.linalg.norm(p2-p3)
p1p3 = numpy.linalg.norm(p1-p3)

print("p1p2 =",p1p2)
print("p2p3 =", p2p3)
print("p1p3 =", p1p3)

if ((p1p2 + p2p3) == p1p3):
    print("Colinearity Established\n")
else:
    print("No Colinearity \n")

#l1 = Line(p1, p2)

#p1 = plot(x, show=False)
#p2 = plot(-x +5, show=False)
##p3 = plot(x +10, show=False)
#p1.append(p2[0])

#p1.show()

