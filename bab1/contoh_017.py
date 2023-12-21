#!/usr/bin/env python

"""
contoh_017.py

Plot 3D

SHSH <sandy.herho@email.ucr.edu>
12/20/23
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

plt.style.use("ggplot")  # agar tampilan lebih menarik

# data
x = np.array([2.1, 3.2, 6, 9.5, 10, 12])
y = np.array([4.1, 6, 37, 70, 92, 100])
z = np.array([6, 6, 9, 15, 14, 13.])

plt.close("all")  # tutup plot sebelumnya

fig = plt.figure(1)
ax = plt.axes(projection="3d")
ax.plot(x, y, z, "-o")
ax.set_title("Plot 3D")
ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$y$")
ax.set_zlabel(r"$z$")

plt.savefig("../gambar/gambar013.png", dpi=250)