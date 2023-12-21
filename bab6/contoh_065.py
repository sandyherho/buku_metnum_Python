#!/usr/bin/env python

"""
contoh_065.py

Metode Gauss-Seidel

SHSH <sandy.herho@email.ucr.edu>
12/19/23
"""

import numpy as np

a = np.array([[4, 1, 2, -1],
             [3, 6, -1, 2],
             [2, -1, 5, -3],
             [4, 1, -3, -8]],float)

b = np.array([2, -1, 3, 2], float)
(n,) = np.shape(b) 
x = np.full(n, 1.0, float) # tebakan awal = 1

beda_x = np.empty(n, float) # beda x setiap 2 iterasi
batas_iter = 100
tol = 1.0e-6

# iterasi
for iterasi in range(batas_iter):
    for i in range(n):
        s = 0
        for j in range(n):
            if j != i:
                s += a[i, j]*x[j]
        x_baru = -1/a[i,i] * (s - b[i]) # x_baru -> skalar
        beda_x[i] = abs(x_baru - x[i]) # hitung beda absolut
        x[i] = x_baru # penugasan nilai baru ke x[i]
    if(beda_x < tol).all(): # cek konvergensi u/ seluruh pers.
        break

print("Jumlah iterasi: %d "%(iterasi+1))
print("Solusi SPL:")
print("\n")
print(x)