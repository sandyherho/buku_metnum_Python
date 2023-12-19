#!/usr/bin/env python

"""
contoh_013.py

Fungsi

SHSH <sandy.herho@email.ucr.edu>
12/19/23
"""

# contoh fungsi dengan 1 input, 1 luaran
def konduktivitas(T):
	a = 2150
	b = 1.05
	y = a + b/((T + 273) - 73.15)
	return y

k_10 = konduktivitas(10)
print('Konduktivitas pada T(10): ', k_10)
print('\n')

# contoh fungsi dengan 2 input, 3 luaran
def hipot(x, y):
	z = (x**2 + y**2)**(1/2)
	l = x + y + z
	v = x * y * z * l 
	return z, l, v

z1, l1, v1 = hipot(3, 4)

print('z: ', z1)
print('\n')
print('l: ', l1)
print('\n')
print('v: ', v1)