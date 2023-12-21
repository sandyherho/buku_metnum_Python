#!/usr/bin/env python

"""
contoh_067.py

Penggunaan NumPy & SciPy
untuk SPL

SHSH <sandy.herho@email.ucr.edu>
12/20/23
"""

import numpy as np
from scipy.linalg import solve, inv

A1 = np.array([[0, 7, -1, 3, 1],
           	  [2, 3, 4, 1, 7],
              [6, 2, 0, 2, -1],
              [2, 1, 2, 0, 2],
              [3, 4, 1, -2, 1]],float)

b1 = np.array([5, 7, 2, 3, 4], float)

A2 = np.array([[2, -1, 5, -3],
           	  [4, 1, 2, -1],
              [4, 1, -3, -8],
              [3, 6, -1, 2]],float)

b2 = np.array([3, 2, 2, -1], float)

# metode langsung menggunakan solve()
x1 = solve(A1, b1)
x2 = solve(A2, b2)

print("x1 (langsung): ")
print(x1)
print("x2 (langsung): ")
print(x2)
print("\n")

# metode tdk langsung menggunakan inv() & np.dot()
x1 = np.dot(inv(A1), b1)
x2 = np.dot(inv(A2), b2)

print("x1 (tdk langsung): ")
print(x1)
print("x2 (tdk langsung): ")
print(x2)