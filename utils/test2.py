import numpy as np
import torch
import matplotlib.pyplot as plt
import os





x = 3.14*np.ones((4,8,8))

x1 = torch.tensor(x[:,:,:])


x2 = np.load("testTiles/testData_0_0.npy")


X = x2[:,:,0:4]
Y = x2[:,:,5]

X = torch.tensor(X)
Y = torch.tensor(Y)

f = sorted(os.listdir(os.path.join("testTiles", ".")))

print(f)















'''


class CustomDataset(Dataset):
    def __init__(self,dataDir,transform):
        self.dataDir = dataDir
        self.transform = transform
        self.imagFiles = sorted(os.listdir(os.path.join(data_dir, ".")))


    def __len__(self):
        return len(self.imageFiles)

    def __getitem__(self,idx):
        

        '''
