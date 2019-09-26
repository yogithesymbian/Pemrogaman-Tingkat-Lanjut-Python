# python doesn't have array
# but in module Numpy
# pip install numpy
import numpy as np

baris = 3
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
for i in range(baris):
    if i % 2 == 0:
        for j in range(kolom):
                arr[i, j] = isi
                isi += 1
    else:
        for j in range(kolom):
            arr[i, kolom - j - 1] = isi
            isi += 1

prnt("")
