#!/usr/bin/env python
"""
contoh_078.py

PDB menggunakan SciPy

SHSH <sandy.herho@email.ucr.edu>
12/22/23
"""

import numpy as np 
from scipy.integrate import odeint

# pers. 7.3
dfdy = lambda y, x: x*y
y0 = 1
x = np.linspace(0, 2, 5) # [0, 2], h = 0,5

y = odeint(dfdy, y0, x)
print("Solusi Numerik Pers. 7.3: ", y)

# pers. 7.19
def dy(y, x):
	y, u = y
	dydx = [u, 4*x + 10*np.sin(x) - y]
	return dydx 

y0 = [0, 2]
x = np.arange(np.pi, 2*np.pi, .1) # [pi, 2pi], h = 0,1
sol = odeint(dy, y0, x)
print(sol)