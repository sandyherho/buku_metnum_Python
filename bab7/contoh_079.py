#!/usr/bin/env python

"""
contoh_079.py

Sistem Lorenz

SHSH <sandy.herho@email.ucr.edu>
12/22/23
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
plt.style.use("bmh")

# PDB sistem Lorenz
def lorenz(u, t, sigma, rho, beta):
    x, y, z = u
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return [dxdt, dydt, dzdt]

# fungsi untuk mensimulasikan & plot trayektori & diagram ruang-fasa 3D
def simulasi_lorenz(kondisi_awal, sigma, rho, beta, jangka_waktu):
    # Selesaikan ODE untuk masing-masing kondisi awal
    trayektori = []
    for ic in kondisi_awal:
        solusi = odeint(lorenz, ic, jangka_waktu, args=(sigma, rho, beta))
        trayektori.append(solusi)

    # Plot trayektori awal
    fig_awal, axs_awal = plt.subplots(3, 1, figsize=(10, 8), sharex=True)

    for i, trajektori in enumerate(trayektori):
        axs_awal[0].plot(jangka_waktu, trajektori[:, 0])
        axs_awal[1].plot(jangka_waktu, trajektori[:, 1])
        axs_awal[2].plot(jangka_waktu, trajektori[:, 2])

    axs_awal[0].set_ylabel('$x$', fontsize=16)
    axs_awal[1].set_ylabel('$y$', fontsize=16)
    axs_awal[2].set_ylabel('$z$', fontsize=16)
    axs_awal[2].set_xlabel('Waktu', fontsize=16)

    # Plot perbedaan x, y, z terhadap waktu
    fig_diff, axs_diff = plt.subplots(3, 1, figsize=(10, 8), sharex=True)

    for i, trajektori in enumerate(trayektori[1:]):  # Lewati trajektori pertama
        x_diff = trajektori[:, 0] - trayektori[0][:, 0]
        y_diff = trajektori[:, 1] - trayektori[0][:, 1]
        z_diff = trajektori[:, 2] - trayektori[0][:, 2]

        axs_diff[0].plot(jangka_waktu, x_diff)
        axs_diff[1].plot(jangka_waktu, y_diff)
        axs_diff[2].plot(jangka_waktu, z_diff)

    axs_diff[0].axhline(0, color='black', linestyle='--', linewidth=0.8)  # Tambahkan garis horizontal di y=0
    axs_diff[1].axhline(0, color='black', linestyle='--', linewidth=0.8)
    axs_diff[2].axhline(0, color='black', linestyle='--', linewidth=0.8)

    axs_diff[0].set_ylabel('$\Delta x$', fontsize=16)
    axs_diff[1].set_ylabel('$\Delta y$', fontsize=16)
    axs_diff[2].set_ylabel('$\Delta z$', fontsize=16)
    axs_diff[2].set_xlabel('Waktu', fontsize=16)

    # Plot ruang fasa 3D untuk dua trajektori
    fig_3d = plt.figure(figsize=(10, 8))
    ax_3d = fig_3d.add_subplot(111, projection='3d')

    for i, trajektori in enumerate(trayektori[:2]):  # Plot hanya dua trajektori pertama
        ax_3d.plot(trajektori[:, 0], trajektori[:, 1], trajektori[:, 2], marker='o', label=f'Trajektori {i + 1}')

    ax_3d.set_xlabel('$x$', fontsize=16)
    ax_3d.set_ylabel('$y$', fontsize=16)
    ax_3d.set_zlabel('$z$', fontsize=16)
    ax_3d.legend()

    # Menyimpan gambar dengan fungsi simpan_gambar
    simpan_gambar(fig_awal, '../gambar/gambar075.png')
    simpan_gambar(fig_diff, '../gambar/gambar076.png')
    simpan_gambar(fig_3d, '../gambar/gambar077.png')

# Fungsi untuk menyimpan gambar
def simpan_gambar(fig, filename):
    fig.savefig(filename, dpi=300, bbox_inches='tight')
    print(f"Gambar {filename} disimpan.")

if __name__ == "__main__":
    # Contoh kasus
    kondisi_awal = np.array([[1.0, 1.0, 1.0], [1.0, 1.01, 1.0]])  # Kondisi awal contoh
    sigma = 10.0
    rho = 28.0
    beta = 8.0 / 3.0
    jangka_waktu = np.linspace(0, 25, 1000)

    # Memanggil fungsi simulasi_lorenz
    simulasi_lorenz(kondisi_awal, sigma, rho, beta, jangka_waktu)