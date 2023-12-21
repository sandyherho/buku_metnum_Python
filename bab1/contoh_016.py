#!/usr/bin/env python

"""
contoh_016.py

Plot 2D

SHSH <sandy.herho@email.ucr.edu>
12/20/23
"""

import numpy as np
import matplotlib.pyplot as plt
plt.style.use("ggplot") # biar keren

# Data
x = np.array ([2.1, 3.2, 6,
			    9.5, 10, 12])

y = np.array ([4.1, 6, 37 ,
			    70, 92, 100])

plt.close("all") # tutup plot2 sebelumnya
fig = plt.figure(1) # jumlah figure
plt.plot ( x, y,"b-o", x, y *2, "r--x")
plt.title (r"Plot $x$ vs $y$")
plt.legend ([r"$y$" , r"$2y$"])
plt.xlabel (r'$x$', fontsize=16)
plt.ylabel (r'$y$', fontsize=16)
plt.savefig("../gambar/gambar012.png", dpi=250)