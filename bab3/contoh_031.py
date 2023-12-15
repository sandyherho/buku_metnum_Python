#!/usr/bin/env python

"""
contoh_031.py

Metode Lagrange

SHSH <sandy.herho@email.ucr.edu>
12/15/23
"""

x = [0, 20, 40, 60, 80, 100]
y = [26.0, 48.6, 61.6, 71.2, 74.8, 75.2]
m = len(x)
n = m-1
xp = float(input('Masukkan Waktu : '))
yp = 0
for i in range(n+1):
    L = 1
    for j in range(n+1):
        if j != i:
            L *= (xp - x[j])/(x[i] - x[j])
    yp += y[i]*L
print('Untuk t = %.1f detik, T = %.1f Celcius' % (xp,yp))