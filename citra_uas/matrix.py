import numpy as np
import math

import matplotlib as plt
from scipy import ndimage

mm = 3
dd = 15
yy = 99
yy2 = 99

# mm = 12
# dd = 17
# yy = 19
# yy2 = 99

T = 3
yogi = np.array([[mm,15,dd], [50,15,75],[yy,38,yy]])
comp = np.array([[mm,15,dd], [50,T,75],[yy2,38,yy]])

# prewwit
sx = np.array([[-1,0,1], [-1,0,1],[-1,0,1]])
sy = np.array([[1,1,1], [0,0,0],[-1,-1,-1]])

# sobel
sxss = np.array([[-1,0,1], [-2,0,2],[-1,0,1]])
syss = np.array([[1,2,1], [0,0,0],[-1,-2,-1]])


print("-------------------")
# hasil prewwit
sxn = yogi * sx
syn = yogi * sy
print("sx \n" , sxn )
print("sy \n" , syn )

print("-----------sobel-------------")

# hasil sobl
sxns = yogi * sxss
syns = yogi * syss
print("sx \n" , sxns )
print("sy \n" , syns )

# print("jumlah", np.square(sxn))

print("-------------------")

# print(yogi.min())
mse = (np.square(yogi - comp)).mean()
print("mse",mse)
PIXEL_MAX = 255.0
pnsr = 20 * math.log10(PIXEL_MAX / math.sqrt(mse))
print("pnsr", pnsr)
print("before : ", pnsr / 20)

print(yogi)
print("\n")
dx = ndimage.sobel(yogi,0)
print(dx)
# plt.plot(yogi)
# plt.show()
# x = np.matrix(np.arange(12).reshape((3, 4)))
# print(x.mean)