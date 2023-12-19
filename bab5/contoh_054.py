#!/usr/bin/env python

"""
contoh_054.py

Integrasi Ganda

SHSH <sandy.herho@email.ucr.edu>
12/18/23
"""

f = lambda x, y: x**2 * y + x * y**2 # pendefinisian fungsi

ax = 1 # batas bawah x
bx = 2 # batas atas x
ay = -1 # batas bawah y
by = 1 # batas atas y
nx = 10 # jumlah pembagi di domain x
ny = 10 # jumlah pembagi di domain y
hx = (bx - ax)/nx # step size x
hy = (by - ay)/ny # step size y

S = 0 # inisiasi penjumlahan
for i in range(0, ny+1): # pengulangan integral luar
    if i == 0 or i == ny: 
        p = 1 # faktor dari suku pertama & terakhir
    elif i % 2 == 1: 
        p = 4 # faktor dari suku - suku yg dikalikan 4
    else:
        p = 2 # faktor dari suku suku yg dikalikan 2
    for j in range(0, nx+1): # pengulangan integral dalam
        if j == 0 or j == nx:
            q = 1 # faktor dari suku pertama & terakhir
        elif j % 2 == 1:
            q = 4 # faktor dari suku - suku yg dikalikan 4 
        else:
            q = 2 # faktor dari suku suku yg dikalikan 2 
        S += p*q * f(ax + j*hx, ay + i*hy)
Integral = hx*hy/9 * S
print('Integral = %f' %Integral)
