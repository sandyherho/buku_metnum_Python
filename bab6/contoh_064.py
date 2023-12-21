#!/usr/bin/env python

"""
contoh_064.py

Metode Jacobi

SHSH <sandy.herho@email.ucr.edu>
12/19/23
"""

import numpy as np

a = np.array([[4, 1, 2, -1],
             [3, 6, -1, 2],
             [2, -1, 5, -3],
             [4, 1, -3, -8]],float)

b = np.array([2, -1, 3, 2], float)
(n,) = np.shape(b) # ukuran array

x = np.full(n, 1.0, float)  # tebakan awal = 1
x_baru = np.empty(n, float) # nilai x baru

batas_iter = 100 # batas iterasi
tol = 1.0e-6 # toleransi galat

# iterasi
for iterasi in range(batas_iter):
    for i in range(n):
        s = 0
        for j in range(n):
            if j != i:
                s += a[i, j]*x[j]
        x_baru[i] = -1/a[i,i] * (s - b[i])
    if (abs(x_baru - x) < tol).all(): # kondisi konvergensi
        break
    else:
        x = np.copy(x_baru) # kopi seluruh elemen x_baru ke x

print("Jumlah iterasi: %d "%(iterasi+1))
print("Solusi SPL:")
print("\n")
print(x)