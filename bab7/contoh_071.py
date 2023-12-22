#!/usr/bin/env python

"""
contoh_071.py

Metode Euler (1)

SHSH <sandy.herho@email.ucr.edu>
12/21/23
"""
from math import exp

dfdy = lambda x,y: x*y # dfdy = xy (PDB)
f = lambda x:exp(x**2/2) # solusi analitik 

x = 0 # nilai awal x
xn = 2 # nilai akhir x
y = 1 # nilai y(x = 0)
h = 0.5 # step size
n = int((xn-x)/h) # jumlah step

# tampilkan kolom solusi
print ('x  \t\t y (Euler) \t y (Analitik)')   
print ('%f \t %f \t %f'% (x,y,f(x)))   

for i in range(1,n+1):
    y += dfdy(x, y)*h # kalulasi y berikutnya
    x += h # x berikutnya
    print ('%f \t %f \t %f'% (x,y,f(x)))