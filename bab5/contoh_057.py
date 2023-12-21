#!/usr/bin/env python

"""
contoh_057.py

Integral Monte Carlo (2)

SHSH <sandy.herho@email.ucr.edu>
12/21/23
"""
import numpy as np
import matplotlib.pyplot as plt
plt.style.use("ggplot")
np.random.seed(212)

f = lambda x:np.sin(x) + 1

xs = np.linspace(0, 1.5 * np.pi, 100)
ys = f(xs)

# MC
lebar = 1.5 * np.pi - 0  # lebar: 0 hingga 1,5 pi
sampel = np.random.uniform(low=0, high=lebar, size=1000000)
luas_mc= f(sampel).mean() * lebar
galat = np.std(sampel * lebar) / np.sqrt(sampel.size)

plt.plot(xs, ys, label="$f(x) = \sin{(x)} + 1$")
plt.fill_between(xs, 0, ys, alpha=0.1)
plt.text(1, 0.5, f"Estimasi luas MC: {luas_mc:0.3f}±{galat:0.3f}", fontsize=12)
plt.xlabel("$x$", fontsize=16)
plt.ylabel("$y$", fontsize=16)
plt.legend();
plt.savefig("../gambar/gambar056.png", dpi=250)