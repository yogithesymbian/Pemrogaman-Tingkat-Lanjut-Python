import numpy as np
# import cv2

# deklarasi array
baris = kolom = 5
# uint8 max is 255
arr = np.ndarray(shape=(baris, kolom), dtype='uint8')
arr[:] = 0

# deklarasi variable
atas = kiri = 0
kanan = kolom
bawah = baris
isi = 0

arah = 0
###
# [state $arah condition]
# 0 bawah , 2 kiri
# 1 kanan , 3 atas
# ###

while isi < baris * kolom:
    # isi array ke arah bawah
    if arah == 0:
        kanan -= 1 # for next state will assign from [5-1..1]
        # for i in range(0, 5)
        for i in range(atas,bawah): # kanan is baris(5)
            arr[i, kanan] = isi     # kanan is 5-1 = 4 tetap and i..5 / [0..5]
                                    # and set the value with isi
            isi += 1  # make isi = isi + 1 while condition terpenuh
        # state next ke kiri | 2
        arah = 2
        # untuk ke kiri itu ada loop [1..5]
        # jadi [kanan = kolom] musti di kurang 1
        # jadi arr[0..4] else ya index out of bound
        # ini bisa langsung di set di loopingnya atau init di sini
        bawah -= 1

    # isi array ke arah kiri
    if arah == 2:
        # for i in reversed(range(1,5)): #| range(kanan,kiri)
        #       # atau gunakan func reversed()
        #       # atau gunakan double ::1
      # for i in range(4, -1, -1) | [4..-1, -1]
        for i in range(kanan-1, kiri-1, -1):
            arr[bawah, i] = isi     # kanan is 5 tetap , i = [1..5]
            isi += 1                # sama kayak tadi
        arah = 3  # next ke atas

    # isi array ke arah atas
    if arah == 3:
        for i in range(bawah-1, atas, -1):
            arr[i, kiri] = isi
            isi += 1

        arah = 1

    # isi array ke arah kanan
    if arah == 1:
        for i in range(kiri,kanan): # kanan is kolom(5)
            arr[atas, i] = isi      # atas is 0 tetap and i..5 / [0..5]
                                    # and set the value with isi
            isi += 1                # make isi = isi + 1 while condition terpenuhi
        # kanan -= 1                # arr is start from 5 , -1 for it's
        arah = 0  # state next ke kanan to bawah

        kiri += 1
        atas += 1

# imshow(title, data)
# cv2.imshow("citra", arr)
# cv2.waitKey(0)  # tekan sembarang tombol for close
# cv2.destroyAllWindows()
#     # isi array ke arah atas
print("")