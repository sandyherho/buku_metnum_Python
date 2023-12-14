#!/usr/bin/env python

"""
contoh_028.py

Metode Biseksi Efektif

SHSH <sandy.herho@email.ucr.edu>
12/13/23
"""

y = lambda x: 2*x**2 - 5*x + 3 # pendefinisian fungsi y(x)

x1 = float(input('Masukkan nilai x1: ')) # input x1
x2 = float(input('Masukkan nilai x2: ')) # input x2

y1 = y(x1) # memanggil fungsi y(x1)
y2 = y(x2) # memanggil fungsi y(x2)

if y1*y2 > 0: # cek apakah tandanya sama?
	print('Tidak terdapat akar di interval ini.')
	exit

for i in range(100):
	xh = (x1+x2)/2
	yh = y(xh) # memanggil fungsi y(xh)
	y1 = y(x1) # memanggil fungsi y(x1)
	if abs(y1) < 1.0e-6:
		break
	elif y1*yh < 0:
		x2 = xh
	else:
		x1 = xh

print('Akar: %.5f' %x1)
print('Jumlah biseksi: %d' %(i+1))