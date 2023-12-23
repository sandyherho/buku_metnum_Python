#!/usr/bin/env python

"""
contoh_081.py

PDP Kuantum

SHSH <sandy.herho@email.ucr.edu>
23/12/23
"""

import numpy as np
import matplotlib.pyplot as plt
plt.style.use("bmh")

def atur_profil_energi_potensial(x, L, V0):
    V = np.zeros_like(x)
    V[(x > L / 3) & (x < 2 * L / 3)] = V0
    return V

def atur_hamiltonian(jml_titik, dx, V):
    H = np.zeros((jml_titik, jml_titik))
    H[np.diag_indices(jml_titik)] = 2 / dx**2 + V
    H[np.arange(1, jml_titik), np.arange(0, jml_titik - 1)] = -1 / dx**2
    H[np.arange(0, jml_titik - 1), np.arange(1, jml_titik)] = -1 / dx**2
    return H

def main():
    # Konstanta
    h_bar = 1.0  # Konstanta Planck tereduksi
    m = 1.0  # Massa partikel
    L = 10.0  # Lebar sumur potensial
    V0 = 50.0  # Tinggi penghalang potensial
    jml_titik = 500  # Jumlah titik spasial
    dx = L / (jml_titik - 1)  # Ukuran langkah spasial

    # Diskritisasi koordinat spasial
    x = np.linspace(0, L, jml_titik)

    # Atur profil energi potensial
    V = atur_profil_energi_potensial(x, L, V0)

    # Atur matriks Hamiltonian
    H = atur_hamiltonian(jml_titik, dx, V)

    # Hitung eigenvalues dan eigenvectors
    eigenvalues, eigenvectors = np.linalg.eigh(H)

    # Plot energi potensial dan beberapa fungsi gelombang pertama
    plt.plot(x, V, label='Energi Potensial')
    for i in range(3):
        plt.plot(x, eigenvalues[i] + eigenvectors[:, i], label=f'Mode Eigen {i+1}')

    plt.xlabel('$x$', fontsize=16)
    plt.ylabel('Energi / Fungsi Gelombang', fontsize=16)
    plt.legend()
    plt.savefig("../gambar/gambar082.png", dpi=250)

if __name__ == "__main__":
    main()