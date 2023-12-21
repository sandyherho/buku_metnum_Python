#!/usr/bin/env python

"""
contoh_066.py

Dominasi Diagonal

SHSH <sandy.herho@email.ucr.edu>
12/20/23
"""

import numpy as np

A = np.array([[2, -1, 5, -3],
           [4, 1, 2, -1],
           [4, 1, -3, -8],
           [3, 6, -1, 2]],float)

b = np.array([3, 2, 2, -1], float)

(n,) = np.shape(b)
x = np.full(n, 1.0, float) # tebakan awal x = 1

beda_x = np.empty(n, float)
batas_iter = 100
tol = 1.0e-6

# iterasi
for iterasi in range(batas_iter):
    for i in range(n):
        s = 0
        for j in range(n):
            if j != i:
                s += A[i, j]*x[j]
        x_baru = -1/A[i,i] * (s - b[i])
        beda_x = abs(x_baru - x[i])
        x[i] = x_baru
    if(beda_x < tol).all():
        break

print("Jumlah iterasi: %d"%(iterasi+1))
print("Solusi SPL: ")
print(x)
