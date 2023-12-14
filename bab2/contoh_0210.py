#!/usr/bin/env python

"""
contoh_0210.py

Metode Garis Potong

SHSH <sandy.herho@email.ucr.edu>
12/14/23
"""

def gar_tong(fn, x=list(), tol=1.0e-9, maxiter=100):
	[x1, x2] = x
	for iterasi in range(maxiter):
		x_baru = x2 - (x2 - x1)/(fn(x2) - fn(x1)) * fn(x2)
		if abs(x_baru - x2) < tol:
			break
		x1 = x2
		x2 = x_baru
	else:
		print('Batas iterasi telah dilampaui tanpa ada solusi.')
	return x_baru, iterasi


# definisi fungsi
f = lambda x:2*x**2 -5*x + 3

# eksekusi
sol, iterasi = gar_tong(f, [0, 8], 0.000001)

# tampilkan hasil
print('Akar: %.6f '%sol)
print('Jumlah iterasi: %d '%iterasi)