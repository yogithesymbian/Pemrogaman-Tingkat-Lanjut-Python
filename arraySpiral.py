__authors__ = "DSN Rihart | Yogi"
# python doesn't have array
# but in module Numpy
# pip install numpy
import numpy as np

baris = 6
kolom = 4
# declaration an array
arr = np.ndarray(shape=(baris, kolom), dtype='int64')  # n dimensi array
# citra uint8
# initialize an array
arr[:] = 0  # all
print(arr.shape)

# masukan shape ke variable
a, b = arr.shape
a = arr.shape[0]

print("\n \n")
isi = 0

# define arrah
arah = 0  # 0 kanan , 1 bawah, 2 kiri, 3 atas
atas = kiri = 0
kanan = kolom
bawah = baris

brs = klm = 0
#  while (0 < 3 * 4)
while isi < baris * kolom :
    if arah == 0:
        arr[brs, klm] = isi
        klm += 1

        if klm == kanan:
            arah = 1
            kanan -= 1
            klm = kanan
    elif arah == 1:
        brs += 1
        arr[brs, klm] = isi

        if brs == baris - 1:
            arah = 2
    elif arah == 2:
        klm -= 1
        arr[brs, klm] = isi
        if klm == kiri:
            arah = 3
            bawah -= 1
    isi += 1