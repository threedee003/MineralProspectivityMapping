
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import skimage.io as io


#       :,0:1819



##img1 = plt.imread("cropped/cu.png")
#img2 = plt.imread("cropped/geomag.png")
#img3 = plt.imread("cropped/fe2o3.png")
img4 = plt.imread("cropped/grav.png")
img5 = plt.imread("cropped/target.png")


#

def showImg(img):
    plt.imshow(img)
    plt.show()



def createGray(img):
    a = np.zeros((img.shape[0],img.shape[1]))
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            x = img[i,j,0]
            g = round(255*(1-x))
            a[i,j] = g

    a = abs(1-a)
    return a





def createMap(img):
    a = np.zeros((img.shape[0],img.shape[1]))
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            x = img[i,j,0]
            if x == 253:
                g = 1
            else:
                g = 0
            a[i,j] = g
    return a


ff = createMap(img5)


#io.imsave("groundTruth.png",s)


plt.imshow(ff)
plt.show()


#f = createGray(img5)

#io.imsave("target.png",f)


#x = np.stack((a,a,a),axis = 2)
