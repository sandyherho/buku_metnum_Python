#!/usr/bin/env python

"""
contoh_015.py

Struktur pengulangan & percabangan

SHSH <sandy.herho@email.ucr.edu>
12/20/23
"""
while True:
    input_pengguna = input("Masukkan nomor: ")

    try:
        nomor = int(input_pengguna)
        break  # keluar dari pengulangan while jika tidak bisa dikonversi
    except ValueError:
        print("Nomor-nya ga bener, Bro!")

# cek nomor dengan menggunakan percabangan
if nomor > 0:
    print("Positif")
elif nomor == 0:
    print("Nol")
else:
    print("Negatif.")

# gunakan pengulangan for untuk menampilkan kata
print(f"Tutorial untuk menampilkan 'Atmosphaira!' sebanyak {nomor} kali:")
for _ in range(nomor):
    print("Atmosphaira!")

