# NIM : 17 615 006
__author__ = "Yogi Arif Widodo"
__copyright__ = "(C) 2019"
__version__ = "0.1"
__email__ = "yogirenbox33@gmail.com"
__status__ = "Development"
__codename__ = 'Pemrograman-Tingkat-Lanjut-Python'
__source__ = "https://github.com/yogithesymbian/Pemrograman-Tingkat-Lanjut-Python"
__info__ = "URL scodeid"

import mylib as mlb

# baca teks file
# uji1 == uji2 != uji3
teks1 = mlb.readTextFile("/root/PycharmProject/PemrogamanTingkatLanjut/maemse/uji1.txt")
teks2 = mlb.readTextFile("/root/PycharmProject/PemrogamanTingkatLanjut/maemse/uji3.txt")

# print(teks1)

# hitung nilai mae
mae = mlb.hitungMAE(teks1, teks2)
mse = mlb.hitungMSE(teks1, teks2)

if mae < 0:
    print("[MAE]Ukuran file tidak sama")
else:
    print("nilai MAE: ", mae)

if mse < 0:
    print("[MSE]Ukuran file tidak sama")
else:
    print("nilai MSE: ", mse)

print("done breakpoint")