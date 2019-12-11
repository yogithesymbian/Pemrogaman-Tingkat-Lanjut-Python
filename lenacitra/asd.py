import cv2

img = cv2.imread('/root/PycharmProject/PemrogamanTingkatLanjut/lenacitra/lenalr.jpeg')
# baris, kolom, layer = img.shape
# pixel berapa komponen berapa
# baris, kolom = img.shape[:2]  # slicing a value

# for i in range(baris):
#     for j in range(kolom):
#         print(img[i,j,0], format(img[i,j,0], '08b')


cv2.imshow("lena",img)
cv2.waitKey(0)
cv2.destroyWindow()
# berapa lebar dan tingginya gunakan sh
# shape ( baris, kolom , layer ) | Shape( 255,255,3)
# 0011.0101
# msg.lsb