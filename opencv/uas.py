# import cv2

# img = cv2.imread("/root/PycharmProject/PemrogamanTingkatLanjut/opencv/index.jpeg", 0)
# # cv2.rectangle(img, (250,30), (450,200), (0,255,0), 5)
# cv2.imshow('apakah persegi panjang ?',img)
# cv2.waitKey(0)  # tekan sembarang tombol for close
# print('wait')

import cv2 as cv
import numpy as np

img = np.zeros((512,512,3), np.uint8) #draw a red line
# img = cv.line(img, (100,100), (300,300), (0,0,255),4)
cv.rectangle(img, (250,30), (450,200), (0,255,0), 5)
cv.imshow('Draw01',img)
cv.waitKey(0)
print("as")