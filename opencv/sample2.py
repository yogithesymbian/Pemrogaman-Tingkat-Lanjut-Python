import numpy as np
import cv2

# load image in grayscale
img = cv2.imread("/root/PycharmProject/PemrogamanTingkatLanjut/opencv/index.jpeg", 0)

cv2.imshow("image", img) # imshow(title, data)
cv2.waitKey(0) # tekan sembarang tombol for close
cv2.destroyAllWindows() # clear cache data