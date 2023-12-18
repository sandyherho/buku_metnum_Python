#!/usr/bin/env python

"""
contoh_042.py

Metode Beda Hingga

SHSH <sandy.herho@email.ucr.edu>
12/17/23
"""

import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

f = lambda x:0.1*x**5 - 0.2*x**3 + 0.1*x - 0.2
h = 0.05
x = np.linspace(0,1,11)

# Beda tengah
dfc1 = (f(x+h) - f(x-h))/(2*h)
dfc2 = (f(x+h) - 2*f(x) + f(x-h)) / h**2

# Plotting 
plt.plot(x,f(x),'-', x,dfc1,'--', x,dfc2,'-.')
plt.xlabel('$x$', fontsize=16)
plt.ylabel('$y$', fontsize=16)
plt.legend(['f(x)','f \'(x)','f \'\'(x)'])
plt.savefig('../gambar/gambar042.png', dpi=250)
