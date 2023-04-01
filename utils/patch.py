from PIL import Image
from itertools import product
import os
import numpy as np



def tile(filename, dir_in, dir_out, d):
    name, ext = os.path.splitext(filename)
    img = np.load(os.path.join(dir_in, filename))
    w, h = img.shape[0],img.shape[1]

    grid = product(range(0, h-h%d, d), range(0, w-w%d, d))
    for i, j in grid:
        np.save(os.path.join(dir_out, f'{name}_{i}_{j}{ext}'),img[j:j+d,i:i+d,:])

pathIN = r'.\finalData'
pathOut = r'.\testTiles'
file = r'testData.npy'
tile(file,pathIN,pathOut,64)
