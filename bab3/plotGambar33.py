#!/usr/bin/env python

"""
plotGambar33.py

Plot Lagrange vs Linier

SHSH <sandy.herho@email.ucr.edu>
12/15/23
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange

# data
x = np.arange(0, 101, 20)
y = [26.0, 48.6, 61.6, 71.2, 74.8, 75.2]

# interpolasi linier
linear_interp = np.interp(x, x, y)

# interpolasi Lagrange suku banyak = 5
lagrange_poly = lagrange(x, y)
lagrange_interp = lagrange_poly(x)

# plot
plt.figure(figsize=(8, 6))

# plot data
plt.scatter(x, y, label='Data', color='blue')

# plot interpolasi linier 
plt.plot(x, linear_interp, label='Interpolasi Linier', linestyle='--', color='green')

# plot interpolasi Lagrange
x_interp = np.linspace(min(x), max(x), 1000)
plt.plot(x_interp, lagrange_poly(x_interp), label='Interpolasi Lagrange (derajat 5)', linestyle='-', color='red')

# tambah label & legenda
plt.xlabel('Waktu [s]', fontsize=16)
plt.ylabel('Temperatur [$^{\circ}$C]', fontsize=16)
plt.legend()
plt.grid()
plt.savefig('../gambar/gambar033.png', dpi=250)