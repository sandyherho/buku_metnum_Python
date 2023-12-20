#!/usr/bin/env python

"""
contoh_062.py

Metode Eliminasi Gauss (2)

SHSH <sandy.herho@email.ucr.edu>
12/19/23
"""

import numpy as np

a = np.array([[0, 7, -1, 3, 1],
           	 [2, 3, 4, 1, 7],
             [6, 2, 0, 2, -1],
             [2, 1, 2, 0, 2],
             [3, 4, 1, -2, 1]],float)

b = np.array([5, 7, 2, 3, 4], float)
n = len(b)
x = np.zeros(n, float)

# Eliminasi
for k in range(n-1):
    if a[k, k] == 0:
        for j in range (n):
            a[k,j], a[k+1, j] = a[k+1, j], a[k,j]
        b[k], b[k+1] = b[k+1], b[k]
    for i in range(k+1, n):
        if a[i, k] == 0: continue
        fktr = a[k, k] / a[i, k]
        b[i] = b[k] - fktr*b[i]
        for j in range(k, n):
            a[i, j] = a[k, j] - fktr*a[i, j]
        
# Substitusi ulang
x[n-1] = b[n-1] / a[n-1, n-1]
for i in range(n-2, -1, -1):
    suku = 0
    for j in range(i+1, n):
        suku += a[i, j]*x[j]
    x[i] = (b[i] - suku)/a[i, i]

print("Solusi SPL:")
print("\n")
print(x)