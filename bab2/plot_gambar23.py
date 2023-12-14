#!/usr/bin/env python

"""
plot_gambar23.py

Menghasilkan gambar 2.3

SHSH <sandy.herho@email.ucr.edu>
12/12/23
"""
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

x = np.linspace(-0.5, 2.5, 1000)
y = 2*x**2 -5*x + 3

fig = plt.figure(figsize = (10, 5))
plt.plot(x, y)
plt.xlabel('$x$', fontsize=16)
plt.ylabel('$y$', fontsize=16)
plt.tight_layout()
plt.savefig('../gambar/gambar023.png', dpi=300)
