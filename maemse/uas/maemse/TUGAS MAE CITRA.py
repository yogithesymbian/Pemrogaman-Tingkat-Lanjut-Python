"""
Created on Sat Dec  7 17:25:19 2019
Yogi Arif Widodo (17615006) TI 5A
@author: yogi
"""

import numpy as np
import cv2 as cv

citra1 = cv.imread("/root/PycharmProject/PemrogamanTingkatLanjut/maemse/uas/maemse/pemandangan.jpg")
citra2 = cv.imread("/root/PycharmProject/PemrogamanTingkatLanjut/maemse/uas/maemse/pemandangangrey.jpg")
# citra1 = cv.imread("pemandangan.jpg")
# citra2 = cv.imread("pemandangangrey.jpg")

mae = 0
print(citra1.shape, citra2.shape)
if (citra1.shape == citra2.shape):
    mae += np.abs((citra1 - citra2)).mean()
    print("Nilai MAE : ", mae)
else:
    print("ukuran berbeda")
