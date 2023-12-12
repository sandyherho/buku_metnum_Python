#!/usr/bin/env python

"""
contoh_022.py

Perhitungan metode iterasi sederhana
dengan derajat ketelitian

SHSH <sandy.herho@email.ucr.edu>
12/12/23
"""

x = 0 # tebakan awal
for iterasi in range(1,101): # asumsi: iterasi 100x cukup! 
	x_baru = (2*x**2 + 3)/5 # menghitung dan mengeluarkan nilai x_baru
	if abs(x - x_baru) < 0.000001: # kondisi derajat ketelitian
		break # keluar dari pengulangan for
	x = x_baru # penugasan nilai x_baru ke x
print('Akar: %.5f' %x_baru) # menampilkan akar hingga keakurasian 5 digit
print('Jumlah iterasi: %d' %iterasi) # menampilkan jumlah iterasi