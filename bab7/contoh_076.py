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
def euler_method(x, y, h, n):
    results = [(x, y)]
    for _ in range(n):
        y += h * dfdy(x, y)
        x += h
        results.append((x, y))
    return results

# Metode RK2 (Runge-Kutta orde 2)
def rk2_method(x, y, h, n):
    results = [(x, y)]
    for _ in range(n):
        K1 = h * dfdy(x, y)
        K2 = h * dfdy(x + h/2, y + K1/2)
        y += K2
        x += h
        results.append((x, y))
    return results

# Metode RK4 (Runge-Kutta orde 4)
def rk4_method(x, y, h, n):
    results = [(x, y)]
    for _ in range(n):
        K1 = h * dfdy(x, y)
        K2 = h * dfdy(x + h/2, y + K1/2)
        K3 = h * dfdy(x + h/2, y + K2/2)
        K4 = h * dfdy(x + h, y + K3)
        y += (K1 + 2*K2 + 2*K3 + K4) / 6
        x += h
        results.append((x, y))
    return results

# Solusi Analitik
def analytic_solution(x_start, x_end, h):
    x_values = np.arange(x_start, x_end + h, h)
    y_values = [f(x) for x in x_values]
    return list(zip(x_values, y_values))

# Parameter
x_start = 0
x_end = 2
y0 = 1
h = 0.5
n = int((x_end - x_start) / h)

# Metode Euler
euler_results = euler_method(x_start, y0, h, n)

# Metode RK2
rk2_results = rk2_method(x_start, y0, h, n)

# Metode RK4
rk4_results = rk4_method(x_start, y0, h, n)

# Solusi Analitik
analytic_results = analytic_solution(x_start, x_end, h)

# Print hasil
print("x \t\t y (Euler) \t y (RK2) \t y (RK4) \t y (analitik)")
for i in range(n+1):
    print("%f \t %f \t %f \t %f \t %f" % (euler_results[i][0], euler_results[i][1], rk2_results[i][1], rk4_results[i][1], analytic_results[i][1]))

# Plot hasil
plt.plot(*zip(*analytic_results), label='Analitik', linewidth=2, color="black")
plt.plot(*zip(*euler_results), label='Euler', linestyle= "dashdot")
plt.plot(*zip(*rk2_results), label='RK2', linestyle= "dashdot")
plt.plot(*zip(*rk4_results), label='RK4', linestyle= "dashdot")
plt.xlabel('$x$', fontsize=16)
plt.ylabel('$y$', fontsize=16)
plt.legend()
plt.savefig("../gambar/gambar073.png", dpi=250)