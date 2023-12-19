#!/usr/bin/env python

"""
contoh_011.py

List, Dictionary, Tuple

SHSH <sandy.herho@email.ucr.edu>
12/19/23
"""

# list
prima = [2, 3, 5, 7, 11, 13]

fitb = ['geologi', 'geodesi', 'oseanografi', 'meteorologi']

nilai = [["Kokom", 80],
         ["Aldi", 100],
         ["Gisma", 75],
         ["Faiz", 57]]

print(prima)

print(fitb[0]) # akses elemen pertama
print(fitb[-1]) # akses elemen terakhir
print(fitb[1:3]) # akses elemen kedua & ketiga

print(nilai[1][1]) # akses nilai Aldi

# dictionary
lulusan = {
    'SHSH':'UMD',
    'MRS':'ITB',
    'NJT':'KU'
}

print(lulusan['MRS']) # akses nilai dari key MRS

# tuple : list tapi konten-nya ga bisa diubah
# kadang bisa digunakan untuk menghemat memori
# tapi tidak akan kita bahas di buku ini

t = ('Meteorologi', 128, 'Oseanografi', 129)

print(t[0]) # akses elemen pertama
print(t[1:]) # akses elemen kedua hingga akhir
