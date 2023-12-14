#!/usr/bin/env python

"""
contoh_021.py

Perhitungan metode iterasi sederhana

SHSH <sandy.herho@email.ucr.edu>
12/12/23
"""

x = 0 # tebakan awal
for iterasi in range(1, 100 + 1): # asumsi: iterasi 100x cukup!
	print(iterasi, x) # menampilkan jumlah iterasi & x
	x_baru = (2*x**2 + 3) / 5 # menghitung dan mengeluarkan nilai x_baru 
	if x == x_baru: # kondisi kesetaraan
		break # keluar dari pengulangan for
	x = x_baru # penugasan nilai x_baru ke x 
print(iterasi, x_baru) # menampilkan jumlah iterasi dan x_baru di akhir pengulangan