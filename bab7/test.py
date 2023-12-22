import numpy as np
import matplotlib.pyplot as plt
plt.style.use("ggplot")

def metode_euler(x0, xn, y0, h):
    dfdy = lambda x, y: x * y  # dfdy = xy (PDB)
    f = lambda x: np.exp(x ** 2 / 2)  # solusi analitik

    n = int((xn - x0) / h)  # jumlah step

    nilai_x = [x0 + i * h for i in range(n + 1)]
    nilai_y = [y0]

    for i in range(1, n + 1):
        y0 += dfdy(x0, y0) * h  # kalulasi y berikutnya
        x0 += h  # x berikutnya
        nilai_y.append(y0)

    return nilai_x, nilai_y

# nilai awal
x0 = 0
xn = 2
y0 = 1

# hitung solusi untuk h=0.5, h=0.2, and h=0.1
nilai_h = [0.5, 0.2, 0.1]

for h in nilai_h:
    nilai_x, nilai_y = metode_euler(x0, xn, y0, h)
    
    # tampilkan hasil
    print(f"\nSolusi untuk h={h}:")
    print("x\t\ty (Euler)\t\ty (Analitik)")
    for x, y, y_analitik in zip(nilai_x, nilai_y, map(lambda x: np.exp(x ** 2 / 2), nilai_x)):
        print(f"{x:.4f}\t{y:.6f}\t{y_analitik:.6f}")

    # plot solusi numerik dengan garis dan titik
    plt.plot(nilai_x, nilai_y, marker='o', linestyle='-', label=f'Euler (h={h})')

# plot solusi analitik
x_analitik = np.linspace(x0, xn, 100)
y_analitik = [np.exp(x ** 2 / 2) for x in x_analitik]
plt.plot(x_analitik, y_analitik, label='Solusi Analitik', linestyle='--')

# tambah label 
plt.xlabel('$x$', fontsize=16)
plt.ylabel('$y$', fontsize=16)
plt.legend()
plt.show()
