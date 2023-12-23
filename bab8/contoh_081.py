#!/usr/bin/env python

"""
contoh_081.py

PDP Laplace 2D

SHSH <sandy.herho@email.ucr.edu>
22/12/23
"""

import numpy as np
import matplotlib.pyplot as plt
plt.style.use("bmh")

def inisialisasi_grid(ukuran, nilai_awal=0):
    return np.full(ukuran, nilai_awal, dtype=float)

def terapkan_kondisi_batas(U):
    Un = 80
    Us = 20
    Uw = 20
    Ue = 0

    U[-1, :] = Un  # Dirichlet
    U[0, :] = Us   # Dirichlet
    U[:, 0] = Uw   # Dirichlet
    U[:, -1] = Ue  # Neumann

def iterasi_laplace(U, V, dxy):
    for i in range(1, U.shape[0]-1, dxy):
        for j in range(1, U.shape[1]-1, dxy):
            U[i, j] = (U[i-1, j] + U[i+1, j] + U[i, j-1] + U[i, j+1]) / 4

def laplace_2d():
    # buat mesh
    X, Y = np.meshgrid(np.arange(0, 50), np.arange(0, 50))

    # inisialisasi
    U = inisialisasi_grid((50, 50))
    V = np.copy(U)

    # kondisi - kondisi batas
    terapkan_kondisi_batas(U)

    # pengaturan iterasi
    dxy = 1
    imax = 1e4

    # iterasi
    ii = 0
    while ii < imax:
        iterasi_laplace(U, V, dxy)
        ii += 1
        galat = np.linalg.norm(U - V) / np.linalg.norm(U)

        np.copyto(V, U)

        if galat < 0.0001:
            break

    return X, Y, U

def plot_kontur(X, Y, U):
    # plot kontur
    kontur = plt.contourf(X, Y, U, 25, cmap="coolwarm")

    # menambahkan garis-garis nilai pada kontur plot
    plt.contour(X, Y, U, colors='black', linestyles='dashed', linewidths=0.5)

    # menambahkan color bar dengan label
    colorbar = plt.colorbar(kontur, label=r'T($^\circ$C)')

    # menambahkan label sumbu x dan y
    plt.xlabel('$x$', fontsize=16)
    plt.ylabel('$y$', fontsize=16)
    plt.savefig("../gambar/gambar081.png", dpi=250)

if __name__ == "__main__":
    X, Y, U = laplace_2d()
    plot_kontur(X, Y, U)
