from PIL import Image, ImageChops
import numpy as np
import matplotlib.pyplot as plt





im = Image.open('CU_300.tif')



# shape : height X Width == 2886 X 4347



'''

im[140:2726,893:3454] for magnetic and gravity

'''

def trim(img):
    img = np.asarray(img)
    x = np.shape(img)[1]
    y = np.shape(img)[0]
    #print(y,x)
    top = 0
    for j in range(0,y):
        if(img[j][x//2] != 255):
            top = j
            break
    bottom = y-top
    print(top,bottom)
    left = 0
    for i in range(x):
        if(img[y//2][i] != 255):
            left = i
            break
    right = x-left
    print(left,right)
    return img[top:bottom,left:right]





im = np.asarray(im)

plt.imsave("",im[140:2726,893:3454],cmap='gray')
