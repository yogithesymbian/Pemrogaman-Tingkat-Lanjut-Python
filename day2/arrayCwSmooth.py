import numpy as np
import cv2

# deklarasi array
baris = kolom = 400
# uint8 max is 255
arr = np.ndarray(shape=(baris, kolom), dtype='uint8')
arr[:] = 0

# deklarasi variable
atas = kiri = 0
kanan = kolom
bawah = baris
isi = 0
arah = 0

counter = 0
decrement = False
# 0 kanan,
# 1 bawah ,
# 2 kiri ,
# 3 atas

while counter < baris * kolom:
    # isi array ke arah kanan
    if arah == 0:
        for i in range(kiri,kanan): # kanan is kolom(5)
            arr[atas, i] = isi  # atas is 0 tetap

            counter += 1

            if decrement:
                isi -= 1
                if isi == 0:
                    decrement = False
            # else: 
            #     isi += 1
            #     if isi == 255:
            #         decrement = True

        kanan -= 1                  # arr is start from 5 , -1 for it's
        arah = 1                    # state next ke bawah

    # isi array ke arah bawah
    if arah == 1:
        # for i in range(5, 8)
        for i in range(atas+1,bawah):   # bawah is baris(5)
            arr[i, kanan] = isi         # kanan is 4 tetap
            counter += 1

            if decrement:
                isi -= 1
                if isi == 0:
                    decrement = False
            else:
                isi += 1
                if isi == 255:
                    decrement = True
        arah = 2                        # state next ke kiri
        bawah -= 1

    # isi array ke arah kiri
    if arah == 2:
        for i in range(kanan-1, kiri-1, -1):
            arr[bawah, i] = isi
            counter += 1

            if decrement:
                isi -= 1
                if isi == 0:
                    decrement = False
            else:
                isi += 1
                if isi == 255:
                    decrement = True
        arah = 3  # next ke atas

    if arah == 3:
        for i in range(bawah-1, atas, -1):
            arr[i, kiri] = isi
            counter += 1

            if decrement:
                isi -= 1
                if isi == 0:
                    decrement = False
            else:
                isi += 1
                if isi == 255:
                    decrement = True
        arah = 0
        kiri += 1
        atas += 1

# imshow(title, data)
cv2.imshow("citra", arr)
cv2.waitKey(0)  # tekan sembarang tombol for close
cv2.destroyAllWindows()
#     # isi array ke arah atas
print("")