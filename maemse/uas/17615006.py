import mylib as mlb

# baca teks file
# uji1 == uji2 != uji3
teks1 = mlb.readTextFile("/root/PycharmProject/PemrogamanTingkatLanjut/maemse/uji1.txt")
teks2 = mlb.readTextFile("/root/PycharmProject/PemrogamanTingkatLanjut/maemse/uji3.txt")

#bandingkan ukuran kedua file
if len(teks1) == len(teks2):
    print("Kedua file memiliki ukuran yang sama")

    #hitung nilai mse
    jmlchar = len(teks1)
    jmlabs = 0

    #hitung jumlah absolute
    for i in range(jmlchar):
        jmlabs = jmlabs + abs(ord(teks1[i]) - ord(teks2[i]))

    mae = jmlabs / jmlchar
    print("jml abs   : ", jmlabs)
    print("nilai mae :", mae)
else:
    print("jumlah gk sama")u