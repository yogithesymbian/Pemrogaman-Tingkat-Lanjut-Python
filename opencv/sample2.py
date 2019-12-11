import numpy as np
import cv2

# load image in grayscale
img = cv2.imread("/root/PycharmProject/PemrogamanTingkatLanjut/opencv/index.jpeg", 0)
imgNormal = cv2.imread("/root/PycharmProject/PemrogamanTingkatLanjut/opencv/index.jpeg")

cv2.namedWindow('image', cv2.WINDOW_NORMAL) # resize result citra img
cv2.imshow("image", img)  # imshow(title, data)
cv2.imshow("imageNormal", imgNormal)  # imshow(title, data)

cv2.waitKey(0)  # tekan sembarang tombol for close

if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite("/root/PycharmProject/PemrogamanTingkatLanjut/opencv/indexgray.jpeg", 0)
    cv2.destroyAllWindows()
cv2.destroyAllWindows() # clear cache data