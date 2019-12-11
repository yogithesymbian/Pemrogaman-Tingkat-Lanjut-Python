import mylib as mlb

# baca teks file
# uji1 == uji2 != uji3
teks1 = mlb.readTextFile("/root/PycharmProject/PemrogamanTingkatLanjut/maemse/uas/uji1.txt")
teks2 = mlb.readTextFile("/root/PycharmProject/PemrogamanTingkatLanjut/maemse/uas/uji3.txt")

isiArrUji1 = 0
isiArrUji2 = 0

#bandingkan ukuran kedua file
if len(teks1) == len(teks2):
    print("Kedua file memiliki ukuran yang sama")

    #hitung nilai mse
    jmlchar = len(teks1)
    jmlabs = 0

    # init assign for rows and cols
    rows, cols = (4, 4)
    # initialize the arr for arr[position][position]
    arr = [[0 for i in range(cols)] for j in range(rows)]

    #hitung jumlah absolute
    for i in range(jmlchar):
        print(teks1[i], teks2[i], ord(teks1[i]), ord(teks2[i]))
        isiArrUji1 = ord(teks1[i])
        isiArrUji2 = ord(teks2[i])
        # arr[1][2] = 12
        for y in range(rows):
            for j in range(cols):
                arr[y][j] = isiArrUji1

        jmlabs = jmlabs + abs(ord(teks1[i]) - ord(teks2[i]))


    for row in arr:
        print("""
                """, row)

    mae = jmlabs / jmlchar
    print("jml abs   : ", jmlabs)
    print("nilai mae :", mae)
else:
    print("jumlah gk sama")