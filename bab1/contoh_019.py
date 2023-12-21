#!/usr/bin/env python

"""
contoh_019.py

Plot Permukaan 3D

SHSH <sandy.herho@email.ucr.edu>
12/20/23
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

plt.style.use("ggplot") # biar keren

# membuat grid
x = np.arange(-2, 2, .05)
y = np.arange (-2, 2, .05)
xx, yy = np.meshgrid(x, y)

# membuat zz untuk seluruh titik
zz = xx * np.exp(-xx**2 - yy**2)

# Plot
plt.close("all")  # tutup plot sebelumnya
fig = plt.figure(1)
ax = plt.axes(projection="3d")
ax.plot_surface (xx, yy, zz, cmap="jet",
					 rstride=1 , cstride =1 , linewidth =0)
ax.set_title("Plot Permukaan 3D")
ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$y$")
ax.set_zlabel(r"$z$")
plt.savefig("../gambar/gambar015.png", dpi=250)