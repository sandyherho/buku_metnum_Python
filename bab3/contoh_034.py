#!/usr/bin/env python

"""
contoh_034.py

Regresi Suku Banyak

SHSH <sandy.herho@email.ucr.edu>
12/17/23
"""

import numpy as np
import matplotlib.pyplot as plt
plt.style.use("ggplot")

# Data
x = np.arange(6)
y = np.array([2, 8, 14, 28, 39, 62], float)

# Regresi polinomial
m = len(x)
n = 3
A = np.zeros((n+1, n+1))
B = np.zeros(n+1)

for baris in range(n+1):
    for kolom in range(n+1):
        if baris == 0 and kolom == 0:
            A[baris, kolom] = m
            continue
        A[baris, kolom] = np.sum(x**(baris+kolom))
    B[baris] = np.sum(x**baris * y)

a = np.linalg.solve(A, B)

# Tampilkan persamaan regresi
print ('Suku Banyak:')
print('f(x) = \t %f'%a[0])
for i in range(1, n+1):
    print('\t %+f x^%d' % (a[i],i))

# Plot data dan hasil regresi
plt.scatter(x, y, label='Data')
x_reg = np.linspace(min(x), max(x), 100)
y_reg = sum(a[i] * x_reg**i for i in range(n+1))
plt.plot(x_reg, y_reg, label='Regresi Suku Banyak (Derajat %d)' %n)
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend()
plt.savefig('../gambar/gambar035.png', dpi=250)