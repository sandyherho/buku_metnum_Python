#!/usr/bin/env python

"""
contoh_074.py

Komparasi Metode Euler, RK2, dan Solusi Analitik

SHSH <sandy.herho@email.ucr.edu>
12/21/23
"""

import numpy as np
import matplotlib.pyplot as plt
plt.style.use("ggplot")

# Fungsi yang merepresentasikan persamaan diferensial
dfdy = lambda x, y: x * y

# Solusi analitik dari persamaan diferensial
f = lambda x: np.exp(x**2/2)

# Metode Euler
def metode_euler(h, x0, y0, xn):
    jum_step = int((xn - x0) / h) + 1
    nilai_x = np.linspace(x0, xn, jum_step)
    nilai_y = np.zeros(jum_step)
    nilai_y[0] = y0

    for i in range(1, jum_step):
        nilai_y[i] = nilai_y[i - 1] + h * dfdy(nilai_x[i - 1], nilai_y[i - 1])

    return nilai_x, nilai_y

# Metode RK2
def runge_kutta_2(h, x0, y0, xn):
    jum_step = int((xn - x0) / h) + 1
    nilai_x = np.linspace(x0, xn, jum_step)
    nilai_y = np.zeros(jum_step)
    nilai_y[0] = y0

    for i in range(1, jum_step):
        K1 = h * dfdy(nilai_x[i - 1], nilai_y[i - 1])
        K2 = h * dfdy(nilai_x[i - 1] + h / 2, nilai_y[i - 1] + K1 / 2)
        nilai_y[i] = nilai_y[i - 1] + K2

    return nilai_x, nilai_y

# Parameter
x0 = 0
xn = 2
y0 = 1
h = 0.5

# Metode Euler
x_euler, y_euler = metode_euler(h, x0, y0, xn)

# Metode RK2
x_rk2, y_rk2 = runge_kutta_2(h, x0, y0, xn)

# Solusi analitik
x_analitik = np.linspace(x0, xn, 100)
y_analitik = f(x_analitik)

# Plot hasil
plt.plot(x_analitik, y_analitik, label='Solusi Analitik')
plt.plot(x_euler, y_euler, 'o-', label='Metode Euler (h=0,5)')
plt.plot(x_rk2, y_rk2, 's-', label='Metode RK2 (h=0,5)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.savefig("../gambar/gambar072.png", dpi=250)