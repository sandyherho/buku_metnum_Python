"""
contoh_025.py

Divergensi

SHSH <sandy.herho@email.ucr.edu>
12/12/23
"""

import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

fn = lambda x:  1/np.cos(x) # definisi fungsi 

# list yang digunakan untuk plotting
xlist = list()
xlist_baru = list()
itrlist = list()

x = 0
for iterasi in range(1, 50):
    x_baru = fn(x)

    # untuk plotting
    xlist.append(x)
    xlist_baru.append(x_baru)
    itrlist.append(iterasi)

    # kondisi konvergensi
    if abs(x_baru - x) < 0.000001:
        break
    x = x_baru

print('Akar: %0.5f' %x_baru)
print('Jumlah iterasi: %d' %iterasi)

# plotting
plt.plot(itrlist, xlist, '-o', itrlist, xlist_baru,'-*')
plt.legend(['$x$','$x_{baru}$'],loc = 'lower right')
plt.xlabel('Iterasi', fontsize=16)
plt.ylabel(r'$x$', fontsize=16)
plt.tight_layout()
plt.savefig('../gambar/gambar022.png', dpi=300)
