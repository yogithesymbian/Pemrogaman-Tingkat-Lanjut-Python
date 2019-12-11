import numpy as np
import cv2

# deklarasi array
baris = kolom = 4
# uint8 max is 255
arr = np.ndarray(shape=(baris, kolom), dtype='uint8')
arr[:] = 0

# deklarasi variable
atas = kiri = 0
kanan = kolom
bawah = baris
isi = 0 # for value init

arah = 0
###
# [state -> #arah condition]
# 0 kanan , 2 kiri
# 1 bawah , 3 atas
# ###

# while 0 < 5 * 5
while isi < baris * kolom:
    # isi array ke arah kanan
    if arah == 0:
        for i in range(kiri,kanan): # kanan is kolom(5)
            arr[atas, i] = isi      # atas is 0 tetap and i..5 / [0..5]
                                    # and set the value with isi
            isi += 1                # make isi = isi + 1 while condition terpenuh
        # set the state for next ke bawah
        arah = 1
        # untuk ke bawah itu ada loop [1..5]
        # jadi [kanan = kolom] musti di kurang 1
        # jadi arr[0..4] else ya index out of bound
        kanan -= 1

    if arah == 1:
        # for i in range(1, 5) | [0..4]
        for i in range(atas+1,bawah):   # bawah is baris(5)    / [1..5]
            arr[i, kanan] = isi         # kanan is 5 tetap , i = [1..5]
            isi += 1
        # set the state for next ke kiri
        arah = 2
        bawah -= 1 # sama kayak sebelumnya

    # isi array ke arah kiri
    if arah == 2:
        for i in range(kanan-1, kiri-1, -1):
            arr[bawah, i] = isi
            isi += 1
        arah = 3  # next ke atas

    # isi arr ke arah atas
    if arah == 3:
        for i in range(bawah-1, atas, -1):
            arr[i, kiri] = isi
            isi += 1
        arah = 0    # condition is terpenuhi
                    # so re-check arah 0
                    # but tidak di line yang sama hingga arah terpenuhi
                    # add +1 for arrow
        kiri += 1
        atas += 1

# imshow(title, data)
cv2.namedWindow('citra', cv2.WINDOW_NORMAL) # resize result citra img
cv2.imshow("citra", arr)
cv2.waitKey(0)  # tekan sembarang tombol for close
cv2.destroyAllWindows()
#     # isi array ke arah atas
print("")