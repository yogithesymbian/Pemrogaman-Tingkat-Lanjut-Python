# NIM : 17 615 006
"""
resource image : https://www.theartstory.org/images20/new_design/bio_box/bio_box_abstract_expressionism.jpg?1
____________________________________________________
Skenario Citra :
uji 1 = abstract_expressionism_safe.jpg
uji 2 = abstract_expressionism_safe_suspicous.jpg

uji 1 dan ujia 2 di convert ke L / grayscale

uji 1 adalah gambar normal
uji 2 adalah gambar yang telah di rusak ( editing red rectangle dan huruf text tersamarkan oleh gambar ; menggunakan inkspace tools)

____________________________________________________
"""
__author__ = "Yogi Arif Widodo"
__copyright__ = "(C) 2019"
__version__ = "0.1"
__email__ = "yogirenbox33@gmail.com"
__status__ = "Development"
__codename__ = 'Pemrograman-Tingkat-Lanjut-Python'
__source__ = "https://github.com/yogithesymbian/Pemrograman-Tingkat-Lanjut-Python"
__info__ = "URL scodeid"

import numpy as np
import cv2

# load image in normal
citraUji1 = cv2.imread("/root/PycharmProject/PemrogamanTingkatLanjut/maemse/uas/abstract_expressionism_safe.jpg")
citraUji2 = cv2.imread("/root/PycharmProject/PemrogamanTingkatLanjut/maemse/uas/abstract_expressionism_safe_suspicous.jpg")

# initialize the result
mse = mae = 0

print(citraUji1.shape, citraUji2.shape)

if (citraUji1.shape == citraUji2.shape):
    mae += np.abs((citraUji1 - citraUji2)).mean()
    mse += ((citraUji1-citraUji2)**2).mean()
    print("Nilai MAE : ", mae)
    print("Nilai MSE : ", mae)
else:
    print("ukuran berbeda")

# cv2.namedWindow('image', cv2.WINDOW_NORMAL) # resize result citra img
cv2.imshow("image", citraUji1)          # imshow(title, data)
cv2.imshow("imageNormal", citraUji2)    # imshow(title, data)

cv2.waitKey(0)              # tekan sembarang tombol for close

if k == 27:                 # wait for ESC key to exit
    cv2.destroyAllWindows() # clear cache data
elif k == ord('s'):         # wait for 's' key to save and exit
    cv2.imwrite("/root/PycharmProject/PemrogamanTingkatLanjut/maemse/uas/abstract_expressionism_safe_gray.jpg", 0)
    cv2.destroyAllWindows()
cv2.destroyAllWindows()