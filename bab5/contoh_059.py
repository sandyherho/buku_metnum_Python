#!/usr/bin/env python

"""
contoh_059.py

Integral Monte Carlo (3)

SHSH <sandy.herho@email.ucr.edu>
12/21/23
"""

import numpy as np
from scipy.integrate import simps
from scipy.stats import norm
import matplotlib.pyplot as plt
plt.style.use("ggplot")
np.random.seed(212)

f = lambda xs:(1 + xs**2) * np.exp(-(xs**4)/4) / np.sqrt(2 * np.pi)

# integrasi MC
x_samp = norm.rvs(size=2000)
p_x = norm.pdf(x_samp)
nilai = f(x_samp) / p_x
luas = nilai.mean()
galat = np.std(nilai) / np.sqrt(nilai.size)

# integrasi Simpson
xs = np.linspace(-5, 5, 200)
ys = f(xs)
luas_simps = simps(ys, x=xs)

# plotting
plt.plot(xs, ys, label=r"$\frac{x^2 + 1}{\sqrt{2\pi}} e^{-\frac{x^4}{4}}$", lw=3)
plt.fill_between(xs, 0, ys, alpha=0.1)
plt.text(-4.8, 0.5, f"Luas MC: {luas:0.2f}±{galat:0.2f}", fontsize=12)
plt.text(-4.8, 0.43, f"Luas Simpson: {luas_simps:0.2f}", fontsize=12)
plt.plot((x_samp, x_samp), ([0 for i in x_samp], [f(i) for i in x_samp]), 
         c='#e89a1c', lw=0.2, ls='-', zorder=-1, alpha=0.3)
plt.xlabel("$x$", fontsize=12)
plt.ylabel("$f(x)$", fontsize=12) 
plt.legend()
plt.savefig("../gambar/gambar058.png", dpi=250)