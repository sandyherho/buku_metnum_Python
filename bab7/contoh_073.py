#!/usr/bin/env python

"""
contoh_073.py

Metode RK2 (1)

SHSH <sandy.herho@email.ucr.edu>
12/21/23
"""

from math import exp

dfdy = lambda x,y: x*y
f = lambda x: exp(x**2/2)

x = 0
xn = 2
y = 1
h = 0.5
n = int((xn-x)/h)

print ('x  \t\t y (RK2) \t y (analitik)')  
print ('%f \t %f \t %f'% (x,y,f(x)))   

# pengulangan utama 
for i in range(1,n+1):
    K1 = h*dfdy(x, y)
    K2 = h*dfdy(x + h/2, y + K1/2)
    y += K2
    x += h
    print ('%f \t %f \t %f'% (x,y,f(x)))