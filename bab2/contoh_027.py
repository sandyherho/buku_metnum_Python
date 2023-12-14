#!/usr/bin/env python

"""
contoh_027.py

Metode Biseksi

SHSH <sandy.herho@email.ucr.edu>
12/13/23
"""

x1 = 0  # nilai pertama di interval             
x2 = 1.2 # nilai kedua di interval            
y1 = 2*x1**2-5*x1+3 # perhiungan y1
y2 = 2*x2**2-5*x2+3 # perhitungan y2

if y1*y2 > 0: # tes apa tandanya sama?       
    print('Tidak ditemukan akar pada interval ini.')
    exit # program berhenti            

for i in range(1,101): # asumsi: 100 biseksi cukup!
    xh = (x1+x2)/2 # hitung nilai tengah
    yh = 2*xh**2-5*xh+3 # hitung yh
    y1 = 2*x1**2-5*x1+3 # hitung y1
    if abs(y1) < 1.0e-6: # kondisi mendekati solusi?
        break # keluar dari pengulangan
    elif y1*yh < 0: # lihat apa tanda berubah pada paruh pertama
        x2 = xh # x2 titik tengah
    else: # lihat apa tanda berubah pada paruh kedua
        x1 = xh # x1 titik tengah
print('Akar: %.5f' %x1)
print('Jumlah biseksi: %d' %i)