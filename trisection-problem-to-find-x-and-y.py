import os
import time
import math 
import numpy
from sympy import Point, Line

p = Point(4,-1)
q = Point(-2,-3)

m1 = 1
n1 = 2

m2 = 2
n2 = 1


x1 = (m1*q[0] +  n1*p[0])/(m1+n1)
y1 = (m1*q[1] + n1*p[1])/(m1+n1)  

x2 = (m2*q[0] +  n2*p[0])/(m1+n1)
y2 = (m2*q[1] + n2*p[1])/(m2+n2)


print(" x1 and y1 is...",x1,"and", y1, "respectively")
print(" x2 and y2 is...",x2,"and", y2, "respectively")






