# baca citra konversi bit
import cv2
import mylib as my

img = cv2.imread('/root/PycharmProject/PemrogamanTingkatLanjut/lenacitra/lenalr.jpeg')
# baris, kolom, layer = img.shape
# pixel berapa komponen berapa
baris, kolom = img.shape[:2]  # slicing a value

stego = img.copy()

# pesan = "Samarinda kota tepian sudah punya bandara sejak tahun 2018"
fileteks = "/root/PycharmProject/PemrogamanTingkatLanjut/lenacitra/teksuji.txt"
pesan = my.readTextFile(fileteks)
print(pesan)
br = kl = 0

for ch in pesan:
    bits = format(ord(ch), '08b')  # biner dari huruf pada pesan

    for bit in bits:
        stgdat = format(stego[br, kl, 0], '08b')[:-1]  #ambil 7 bit dari citra
        stgdat = stgdat + bit  # tabahkan dengan 1 bit pesan
        stego[br, kl, 0] = int(stgdat,2)# simpan data

        kl += 1
        if kl == kolom:
            br += 1
            kl = 0


# save stegoimage
cv2.imwrite("lenastego.png", img)
# cv2.imshow('lenastego', img)
# cv2.imshow('lena', img)
# cv2.waitKey(0)
# cv2.destroyWindow()
# berapa lebar dan tingginya gunakan sh
# shape ( baris, kolom , layer ) | Shape( 255,255,3)
# 0011.0101
# msg.lsb
stegox = stego
# stegox = cv2.imread("lenastego.png")
# baris, kolom = stegox.shape[:2]

jmlhuruf = 647
pesan = ""

br = kl = 0
bits = ""

while len(pesan) < jmlhuruf:
    # ambil satu bit teakhir
    # print(br, kl, end="\t")
    bit = format(stegox[br, kl, 0], '08b')[-1]
    bits = bits + bit

    # konversi menjadi huruf, dan gabungkan
    if (len(bits)==8):
        huruf = chr(int(bits, 2))
        pesan = pesan + huruf
        bits = ""

    # ubah posisi kolom dan baris
    kl += 1
    if kl == kolom:
        br += 1
        kl = 0

print("\n\n")
print(pesan)