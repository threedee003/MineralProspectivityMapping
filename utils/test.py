import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import skimage.io as io
import pandas as pd
import time


img = io.imread("AMAG_300_15_CLASS.tif")

plt.imshow(img[140:2726,893:3454])
plt.show()



# x1 = io.imread("originals/CU_300.tif")
# x2 = io.imread("originals/FE2O3_300.tif")
# x3 = io.imread("originals/GGRAV_300.tif")
# x4 = io.imread("originals/GMAG_300.tif")
# x5 = io.imread("originals/MNO_300.tif")
#
# x7 = io.imread("groundTruth.png")
#
#
#
#
# x1 = x1[140:2726,893:3454]
# x2 = x2[140:2726,893:3454]
# x3 = x3[140:2726,893:3454]
# x4 = x4[140:2726,893:3454]
# x5 = x5[140:2726,893:3454]
#
#
#
#
#
# x = np.stack((x1,x2,x3,x4,x5,x7), axis = 2)
#
#
# np.save("testingData",x[1464:1823,1880:2340])




#
# trainDat = np.load("testingData.npy")
#
# n = trainDat.shape[0]
# m = trainDat.shape[1]
#
#
# storage = np.zeros((n*m,8))
# count = 0
#
# st = time.time()
# for i in range(n):
#     for j in range(m):
#         storage[count][0] = i
#         storage[count][1] = j
#         storage[count][2] = trainDat[i][j][0]   # copper
#         storage[count][3] = trainDat[i][j][1]   # iron
#         storage[count][4] = trainDat[i][j][2]   # gravity
#         storage[count][5] = trainDat[i][j][3]   # magnetic
#         storage[count][6] = trainDat[i][j][4]   # manganese
#         storage[count][7] = trainDat[i][j][5]   # groundTruth
#         count += 1
#
#
# print(f"time taken : {time.time()-st} secs")
# np.save("pointFormTest",storage)
