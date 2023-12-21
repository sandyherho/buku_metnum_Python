#!/usr/bin/env python

"""
contoh_058.py

Integral Monte Carlo (3)

SHSH <sandy.herho@email.ucr.edu>
12/21/23
"""
import numpy as np
from scipy.integrate import simps
import matplotlib.pyplot as plt
plt.style.use("ggplot")
np.random.seed(212)

# integrasi MC
sampel = np.random.normal(size=1000)
fmc = 1 + sampel ** 2
luas_mc = fmc.mean()
galat = np.std(fmc) / np.sqrt(fmc.size)

# integrasi Simpson
def f(xs):
    return (1 + xs**2) * np.exp(-(xs**2)/2) / np.sqrt(2 * np.pi)
xs = np.linspace(-5, 5, 200)
ys = f(xs)
luas_simps = simps(ys, x=xs)

# Plotting
plt.plot(xs, ys, label=r"$f(x) = \frac{(x^2 +1)}{\sqrt{2\pi}} e^{-\frac{x^2}{2}}$", lw=3)
plt.fill_between(xs, 0, ys, alpha=0.1)
plt.text(-4.8, 0.5, f"Luas MC: {luas_mc:0.2f}±{galat:0.2f}", fontsize=12)
plt.text(-4.8, 0.43, f"Luas Simpson: {luas_simps:0.2f}", fontsize=12)
plt.plot((sampel, sampel), ([0 for i in sampel], [f(i) for i in sampel]), 
         c='#1c93e8', lw=0.2, ls='-', zorder=-1, alpha=0.5)
plt.xlabel("$x$", fontsize=16)
plt.ylabel("$y$", fontsize=16) 
plt.legend();
plt.savefig("../gambar/gambar057.png", dpi=250)