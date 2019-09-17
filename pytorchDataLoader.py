# PyTorch imports
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torch.autograd import Variable
# our model and solution imports
from model import G, D
from data import AdiosDataLoader

# partition VTK-m rendered images and buffers
train_set = AdiosDataLoader(dataset,split="train")
val_set = AdiosDataLoader(dataset, split="val") 
test_set = AdiosDataLoader(dataset, split="test")
# instantiate PyTorch dataloaders with AdiosDataLoader
train_data = DataLoader(dataset=train_set, num_workers=...,
                        batch_size=..., shuffle=True)
val_data = DataLoader(dataset=val_set, num_workers=...,
                      batch_size=..., shuffle=False)
test_data = DataLoader(dataset=test_set,...)
# cast loaded VTK-m data to PyTorch tensors
gt = torch.FloatTensor(train_batch_size,
                        n_channel_input,
                        256, 256)
direct, albedo, depth, normal =  torch.FloatTensor(...)
                                 , ... , ... , ...
# ground truth labels
label = torch.FloatTensor(train_batch_size)
# instantiate generator and descriminator
netG = G(n_channel_input*4, n_channel_output,
         n_generator_filters)
netD = D(n_channel_input*4, n_channel_output,
         n_discriminator_filters)
# assign to GPU
netD, netG = netD.cuda(),  netG.cuda()
# loss functions:
# Binary Cross Entropy and L1 Loss
criterion, criterion_l1 = nn.BCELoss(), nn.L1Loss()
# Cuda placement
criterion = criterion.cuda()
criterion_l1 = criterion_l1.cuda()
albedo = albedo.cuda()
gt, direct = gt.cuda(), direct.cuda()
depth, normal = depth.cuda(), normal.cuda()
label = label.cuda()
# instantiate PyTorch variables of VTK-m renderings
albedo = Variable(albedo)
gt, direct = Variable(gt), Variable(direct)
depth, normal = Variable(depth), Variable(normal)
label = Variable(label)
# instantiate PyTorch Adam gradiant decent
optimizerD = optim.Adam(netD.parameters(),
                        lr=..., betas=...)
optimizerG = optim.Adam(netG.parameters(),
                        lr=..., betas=...)
def train(epoch):
    for (i, images) in enumerate(train_data):
        netD.zero_grad()
        ...
