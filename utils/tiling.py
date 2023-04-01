
import os
import numpy as np
import torch
from torch.utils.data import Dataset
from PIL import Image



class CustomDataset(Dataset):
    def __init__(self, data_dir, transform=None):
        self.data_dir = data_dir
        self.transform = transform
        self.imageFilenames = sorted(os.listdir(os.path.join(data_dir, "tiles")))

    def __len__(self):
        return len(self.imageFilenames)

    def __getitem__(self, idx):
        imagePath = os.path.join(self.data_dir, "tiles", self.imageFilenames[idx])
        img = np.load(imagePath)
        X = img[:,:,0:5]
        Y = img[:,:,-1]

        # X = torch.tensor(X)
        # Y = torch.tensor(Y)

        if self.transform:
            X = self.transform(X)
            Y = self.transform(Y)

        return X, Y




from torchvision.transforms import transforms

transform = transforms.Compose([
    transforms.ToTensor(),
])

dataset = CustomDataset("trainTiles", transform=transform)
dataloader = torch.utils.data.DataLoader(dataset, batch_size=4, shuffle=True)

# for img,target in dataloader:
#     print(img.size())
#     print(np.unique(img.numpy()))


for i,j in dataloader:
    print(i.size())
    print(j.size())

    break





def trainer(model,trainLoader,validationLoader,epochs,lossFn,optimizer,loss,acc,device):
    model = model.to(device)
    for epoch in range(epochs):
        for img, target in trainLoader:
            img = img.to(device)
            target = target.to(device)
            output = model(img)
