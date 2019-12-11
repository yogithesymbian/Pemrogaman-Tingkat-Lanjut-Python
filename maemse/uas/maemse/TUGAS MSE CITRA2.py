"""
Created on Sat Dec  7 17:29:49 2019
Yogi Arif Widodo (17615006) TI 5A
@author: yogi
"""

import numpy as np
import cv2 as cv

citra1 = cv.imread("pemandangangrey.jpg")
citra2 = cv.imread("pemandangan.jpg")
mse = 0

if(citra1.shape == citra2.shape):
    mse += ((citra1-citra2)**2).mean()
    print("Nilai MSE : ", mse)
else:
    print("ukuran berbeda")
