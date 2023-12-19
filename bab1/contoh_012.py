#!/usr/bin/env python

"""
contoh_012.py

Array

SHSH <sandy.herho@email.ucr.edu>
12/19/23
"""

# mengimpor pustaka
import numpy as np
from scipy.linalg import eig

vek = np.array([1, 2, 8])
print('Vek: ', vek)
print("\n")

# vektor kolom
kol_vek = vek.reshape(-1, 1)
print('kol_vek: ', kol_vek)
print("\n")

kol_vek1 = np.array([[1], [2], [8]])
print('kol_vek1: ', kol_vek1)
print("\n")

kol_vek2 = np.array([[1],
					[2],
			        [8]])
print('kol_vek2: ', kol_vek2)
print("\n")

# matriks
mat = np.array([[1, 2, 6],[3, 4, 9], [1, -2, 7]])
print('mat: ', mat)
print("\n")

mat1 = np.array([[1, 2, 6],
				[3, 4, 9],
				[1, -2, 7]])

print('mat1: ', mat1)
print("\n")

# ekstraksi array
a = vek[2] # ekstrak elemen ketiga
print('a: ', a)
print("\n")

b = vek[:1] # ekstrak elemen 1-2 
print('b: ', b)
print("\n")

c = vek[:] # esktrak seluruh elemen 
print('c: ', c)
print("\n")

d = vek[-1] # ekstrak elemen terakhir
print('d: ', d)
print('\n')

vek_dua = mat[:, 1] # ekstrak kolom kedua
print('vek_dua: ', vek_dua)
print("\n")

dua_satu = mat[1, 0] # ekstrak elemen 2,1 
print('dua_satu: ', dua_satu)
print("\n")

# operasi array
vek2 = vek + vek # penjumlahan
print('Penjumlahan: ', vek2)
print("\n")

vek3 = vek * 2 # perkalian skalar
print('Perkalian skalar: ', vek3)
print("\n")

vek4 = vek * vek # perkalian antar elemen
print('Perkalian antar elemen: ', vek4)
print("\n")

vek5 = np.dot(vek, vek) # perkalian titik
print('Perkalian titik: ', vek5)
print("\n")

vek6 = np.cross(vek, vek) # perkalian silang
print('Perkalian silang: ', vek6)
print('\n')

nilai_eigen, vek_eigen = eig(mat) # dekomposisi eigen
print("Nilai Eigen: ", nilai_eigen)
print("Vektor Eigen: ", vek_eigen)