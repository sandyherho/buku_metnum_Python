#!/usr/bin/env python

"""
contoh_029.py

Metode Regula Falsi

SHSH <sandy.herho@email.ucr.edu>
12/14/23
"""

y = lambda x: 2*x**2 - 5*x + 3 # pendefinisian fungsi y(x)


def rfalsi(fn, x1, x2, tol = 0.001, ilimit = 100):
    y1 = fn(x1)
    y2 = fn(x2)
    xh = 0			
    ipos = 0 			# hitung posisi keliru
    if y1 == 0: xh = x1		# x1 -> akar	
    elif y2 == 0: xh = x2	# x2 -> akar
    elif y1 * y2 > 0:		# jika y1 & y2 mempunyai tanda yg sama
        print('Tidak ditemukan akar pada interval ini.')
    else:    
        for ipos in range(1,ilimit+1):
            xh = x2 - (x2-x1)/(y2-y1) * y2
            yh = fn(xh)
            if abs(yh) < tol:
                break
            elif y1 * yh < 0: # jika y1 & yh mempunyai tanda berlawanan
                x2 = xh
                y2 = yh
            else:
                x1 = xh
                y1 = yh
    return xh, ipos

x1 = float(input('Masukkan x1: '))
x2 = float(input('Masukkan x2: '))
x, n = rfalsi(y,x1,x2)

# Hasil
print('Akar: %f' %x)
print('Jumlah posisi keliru selama perhitungan: %d' %n)
x1 = float(input('Masukkan x1: '))
x2 = float(input('Masukkan x2: '))
x, n = rfalsi(y,x1,x2)

# Tampilkan hasil
print('Akar: %.5f' %x)
print('Jumlah posisi keliru selama perhitungan: %d' %n)