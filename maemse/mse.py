import mylib as mlb

# baca teks file
teks1 = mlb.readTextFile("/root/PycharmProject/PemrogamanTingkatLanjut/maemse/uji1.txt")
teks2 = mlb.readTextFile("/root/PycharmProject/PemrogamanTingkatLanjut/maemse/uji3.txt")

# print(teks1)

# hitung nilai mae
mse = mlb.hitungMSE(teks1, teks2)

if mse < 0:
    print("Ukuran file tidak sama")
else:
    print("nilai MSE: ", mse)