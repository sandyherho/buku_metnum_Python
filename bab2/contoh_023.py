#!/usr/bin/env python

"""
contoh_023.py

Perhitungan metode iterasi sederhana
dengan derajat ketelitian
dengan pengulangan while

SHSH <sandy.herho@email.ucr.edu>
12/12/23
"""
x = 5 # nilai arbitrer
x_baru = 0 # tebakan awal
iterasi = 0
while abs(x_baru - x) >= 0.000001:
    iterasi += 1
    x = x_baru
    x_baru = (2*x**2 + 3)/5
    
print('Akar: %0.5f' %x_baru)
print('Jumlah iterasi: %d' %iterasi)