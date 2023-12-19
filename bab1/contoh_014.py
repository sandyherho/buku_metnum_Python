#!/usr/bin/env python

"""
contoh_014.py

Ekspresi lambda

SHSH <sandy.herho@email.ucr.edu>
12/19/23
"""

# contoh ekspresi lambda dengan 1 input, 1 luaran
konduktivitas = lambda T: 2150 + 1.05 / ((T + 273) - 73.15)
k_10 = konduktivitas(10)
print('Konduktivitas pada T(10): ', k_10)
print('\n')

# contoh ekspresi lambda dengan 2 input, 3 luaran
hipot = lambda x, y: ((x**2 + y**2)**(1/2),\
						x + y + (x**2 + y**2)**(1/2),\
				 		x * y * ((x**2 + y**2)**(1/2))\
				 		* (x + y + (x**2 + y**2)**(1/2)))

z1, l1, v1 = hipot(3, 4)

print('z: ', z1)
print('\n')
print('l: ', l1)
print('\n')
print('v: ', v1)