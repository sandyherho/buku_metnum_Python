#!/usr/bin/env python

"""
contoh_033.py

Regresi Linier

SHSH <sandy.herho@email.ucr.edu>
12/17/23
"""

import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

# Data input
x = np.array([3, 4, 5, 6, 7, 8])
y = np.array([0, 7, 17, 26, 35, 45])

# Jumlah data
n = len(x)

# Menghitung koefisien regresi
alpha = (np.mean(y) * np.sum(x**2) - np.mean(x) * np.sum(x*y)) / (np.sum(x**2) - n * np.mean(x)**2)
beta = (np.sum(x*y) - np.mean(x) * np.sum(y)) / (np.sum(x**2) - n * np.mean(x)**2)

# Persamaan garis regresi linier
gar_reg = alpha + beta * x

# Menampilkan persamaan garis regresi linier
print('Persamaan garis regresi linier: ')
print('f(x) = (%.3f) + (%.3f)x' % (alpha, beta))

# Memplot titik data dan garis regresi linier
plt.scatter(x, y, label='Data')
plt.plot(x, gar_reg, label='Regresi Linier')
plt.xlabel('$x$', fontsize=16)
plt.ylabel('$y$', fontsize=16)
plt.legend()
plt.savefig('../gambar/gambar034.png', dpi=250)


