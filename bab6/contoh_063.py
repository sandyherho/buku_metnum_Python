#!/usr/bin/env python

"""
contoh_063.py

Metode Gauss-Jordan

SHSH <sandy.herho@email.ucr.edu>
12/22/23
"""

import numpy as np

def gssjrdn(a,b):
    a = np.array(a, float)
    b = np.array(b, float)
    n = len(b)

    # pengulangan utama
    for k in range(n):

        # pivoting parsial
        if np.fabs(a[k,k]) < 1.0e-12:
            for i in range(k+1,n):
                if np.fabs(a[i,k]) > np.fabs(a[k,k]):
                    a[[k,i]] = a[[i,k]]
                    b[[k,i]] = b[[i,k]]
                    break
        
        # pembagian pada baris pivot
        pivot = a[k,k]
        a[k] /= pivot
        b[k] /= pivot
        
        # pengulangan eliminasi
        for i in range(n):
            if i == k or a[i,k] == 0: continue
            faktor = a[i,k]
            a[i] -= faktor * a[k]
            b[i] -= faktor * b[k]
    return b,a


a = [[0,2,0,1],
     [2,2,3,2],
     [4,-3,0,1],
     [6,1,-6,-5]]

b = [0,-2,-7,6]

X,A = gssjrdn(a,b)

print("Solusi SPL: ")
print(X)
print("\n")
print("Matriks koefisien sesudah transformasi: ")
print(A)
