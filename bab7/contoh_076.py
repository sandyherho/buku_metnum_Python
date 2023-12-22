#!/usr/bin/env python

"""
contoh_076.py

Metode Analitik vs RK4 vs RK2 vs Euler

SHSH <sandy.herho@email.ucr.edu>
12/21/23
"""
import numpy as np
import matplotlib.pyplot as plt
plt.style.use("bmh")

# Fungsi persamaan diferensial
dfdy = lambda x, y: x * y
f = lambda x: np.exp(x**2/2)

# Metode Euler
def metode_euler(x, y, h, n):
    hasil = [(x, y)]
    for _ in range(n):
        y += h * dfdy(x, y)
        x += h
        hasil.append((x, y))
    return hasil

# Metode RK2 (Runge-Kutta orde 2)
def metode_rk2(x, y, h, n):
    hasil = [(x, y)]
    for _ in range(n):
        K1 = h * dfdy(x, y)
        K2 = h * dfdy(x + h/2, y + K1/2)
        y += K2
        x += h
        hasil.append((x, y))
    return hasil

# Metode RK4 (Runge-Kutta orde 4)
def metode_rk4(x, y, h, n):
    hasil = [(x, y)]
    for _ in range(n):
        K1 = h * dfdy(x, y)
        K2 = h * dfdy(x + h/2, y + K1/2)
        K3 = h * dfdy(x + h/2, y + K2/2)
        K4 = h * dfdy(x + h, y + K3)
        y += (K1 + 2*K2 + 2*K3 + K4) / 6
        x += h
        hasil.append((x, y))
    return hasil

# Solusi Analitik
def solusi_analitik(x_mulai, x_akhir, h):
    nilai_x = np.arange(x_mulai, x_akhir + h, h)
    nilai_y = [f(x) for x in nilai_x]
    return list(zip(nilai_x, nilai_y))

# Parameter
x_mulai = 0
x_akhir = 2
y0 = 1
h = 0.5
n = int((x_akhir - x_mulai) / h)

# Metode Euler
euler_hasil = metode_euler(x_mulai, y0, h, n)

# Metode RK2
rk2_hasil = metode_rk2(x_mulai, y0, h, n)

# Metode RK4
rk4_hasil = metode_rk4(x_mulai, y0, h, n)

# Solusi Analitik
analitik_hasil = solusi_analitik(x_mulai, x_akhir, h)

# Print hasil
print("x \t\t y (Euler) \t y (RK2) \t y (RK4) \t y (analitik)")
for i in range(n+1):
    print("%f \t %f \t %f \t %f \t %f" % (euler_hasil[i][0], euler_hasil[i][1], rk2_hasil[i][1], rk4_hasil[i][1], analitik_hasil[i][1]))

# Plot hasil
plt.plot(*zip(*analitik_hasil), label='Analitik', linewidth=2, color="black")
plt.plot(*zip(*euler_hasil), label='Euler', linestyle= "dashdot")
plt.plot(*zip(*rk2_hasil), label='RK2', linestyle= "dashdot")
plt.plot(*zip(*rk4_hasil), label='RK4', linestyle= "dashdot")
plt.xlabel('$x$', fontsize=16)
plt.ylabel('$y$', fontsize=16)
plt.legend()
plt.savefig("../gambar/gambar073.png", dpi=250)