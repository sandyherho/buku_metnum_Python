#!/usr/bin/env python

"""
contoh_018.py

Plot Kontur

SHSH <sandy.herho@email.ucr.edu>
12/20/23
"""

import numpy as np
import matplotlib.pyplot as plt
plt.style.use("ggplot") # biar keren

# membuat grid
x = np.arange(-2, 2, .05)
y = np.arange (-2, 2, .05)
xx, yy = np.meshgrid(x, y)

# membuat zz untuk seluruh titik
zz = xx * np.exp(-xx**2 - yy**2)

# plot
plt.contourf(xx, yy, zz, cmap="coolwarm")
plt.colorbar()
plt.title ("Plot Kontur")
plt.xlabel (r"$x$", fontsize=16)
plt.ylabel (r"$y$", fontsize=16)
plt.savefig("../gambar/gambar014.png", dpi=250)