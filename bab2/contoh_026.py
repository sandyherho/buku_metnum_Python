#!/usr/bin/env python

"""
contoh_026.py

Metode Newton-Raphson

SHSH <sandy.herho@email.ucr.edu>
12/12/23
"""

x = 0
for iterasi in range(1, 101):
    x_baru = x - (2*x**2 - 5*x + 3)/(4*x - 5) # persamaan Newton-Raphson
    if abs(x_baru - x) < 0.000001:
        break
    x = x_baru
print('Akar: %0.5f' % x_baru)
print('Jumlah iterasi: %d' %iterasi)