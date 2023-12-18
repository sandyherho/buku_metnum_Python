#!/usr/bin/env python

"""
contoh_041.py

Metode Beda Hingga

SHSH <sandy.herho@email.ucr.edu>
12/17/23
"""

f = lambda x:0.1*x**5 - 0.2*x**3 + 0.1*x - 0.2
h = 0.05
x = 0.1

# Beda Maju
dff1 = (f(x+h) - f(x))/h
dff2 = (f(x+2*h) - 2*f(x+h) + f(x))/h**2
print('Solusi dari beda maju:')
print('f\'(%f) = %f'%(x,dff1))
print('f\'\'(%f) = %f'%(x,dff2))

# Beda Tengah
dfc1 = (f(x+h)-f(x-h))/(2*h)
dfc2 = (f(x+h)-2*f(x)+f(x-h))/h**2
print('\nSolusi dari beda tengah:')
print('f\'(%f) = %f'%(x,dfc1))
print('f\'\'(%f) = %f'%(x,dfc2))

# Beda Mundur
dfb1 = (f(x)-f(x-h))/h
dfb2 = (f(x)-2*f(x-h)+f(x-2*h))/h**2
print('\nSolusi dari beda mundur:')
print('f\'(%f) = %f'%(x,dfb1))
print('f\'\'(%f) = %f'%(x,dfb2))