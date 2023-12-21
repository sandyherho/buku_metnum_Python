#!/usr/bin/env python

"""
contoh_055.py

Estimasi kaidah Simpson

SHSH <sandy.herho@email.ucr.edu>
12/20/23
"""

import numpy as np
from scipy.integrate import simps
import matplotlib.pyplot as plt
plt.style.use("ggplot")

f = lambda x:np.sin(x) + 1

xs = np.linspace(0, 1.5 * np.pi, 100)
ys = f(xs)
luas = simps(ys, x=xs)

plt.plot(xs, ys, label=r"$f(x) = \sin{(x)} + 1$")
plt.fill_between(xs, 0, ys, alpha=0.1)
plt.text(1, 0.75, f"Estimasi luas kaidah Simpson: {luas:0.3f}", fontsize=12)

plt.ylabel("$y$", fontsize=16)
plt.xlabel("$x$", fontsize=16)
plt.legend()
plt.savefig("../gambar/gambar054.png", dpi=250)