import torch
import torch.nn as nn
import torch.nn.functional as F


class VGG_nst(nn.Module):
    def __init__(self, pooling=None):
        super(VGG_nst,self).__init__()

        self.conv1_1 = nn.Conv2d(3, 64, kernel_size=3, padding=1)
        self.conv1_2 = nn.Conv2d(64, 64, kernel_size=3, padding=1)
        
        self.conv2_1 = nn.Conv2d(64, 128, kernel_size=3, padding=1)
        self.conv2_2 = nn.Conv2d(128, 128, kernel_size=3, padding=1)
        
        self.conv3_1 = nn.Conv2d(128, 256, kernel_size=3, padding=1)
        self.conv3_2 = nn.Conv2d(256, 256, kernel_size=3, padding=1)
        self.conv3_3 = nn.Conv2d(256, 256, kernel_size=3, padding=1)
        self.conv3_4 = nn.Conv2d(256, 256, kernel_size=3, padding=1)
        
        self.conv4_1 = nn.Conv2d(256, 512, kernel_size=3, padding=1)
        self.conv4_2 = nn.Conv2d(512, 512, kernel_size=3, padding=1)
        self.conv4_3 = nn.Conv2d(512, 512, kernel_size=3, padding=1)
        self.conv4_4 = nn.Conv2d(512, 512, kernel_size=3, padding=1)
        
        self.conv5_1 = nn.Conv2d(512, 512, kernel_size=3, padding=1)
        self.conv5_2 = nn.Conv2d(512, 512, kernel_size=3, padding=1)
        self.conv5_3 = nn.Conv2d(512, 512, kernel_size=3, padding=1)
        self.conv5_4 = nn.Conv2d(512, 512, kernel_size=3, padding=1)
        

        if pooling is 'avg':
            self.pool_1 = nn.AvgPool2d(kernel_size=2, stride=2)
            self.pool_2 = nn.AvgPool2d(kernel_size=2, stride=2)
            self.pool_3 = nn.AvgPool2d(kernel_size=2, stride=2)
            self.pool_4 = nn.AvgPool2d(kernel_size=2, stride=2)
            self.pool_5 = nn.AvgPool2d(kernel_size=2, stride=2)
        else:
            self.pool_1 = nn.MaxPool2d(kernel_size=2, stride=2)
            self.pool_2 = nn.MaxPool2d(kernel_size=2, stride=2)
            self.pool_3 = nn.MaxPool2d(kernel_size=2, stride=2)
            self.pool_4 = nn.MaxPool2d(kernel_size=2, stride=2)
            self.pool_5 = nn.MaxPool2d(kernel_size=2, stride=2)

        
    def forward(self, x, out_layers):
        out = {}
        out['conv1_1'] = F.relu(self.conv1_1(x))
        out['conv1_2'] = F.relu(self.conv1_2(out['conv1_1']))
        out['pool_1'] = self.pool_1(out['conv1_2'])
        
        out['conv2_1'] = F.relu(self.conv2_1(out['pool_1']))
        out['conv2_2'] = F.relu(self.conv2_2(out['conv2_1']))
        out['pool_2'] = self.pool_2(out['conv2_2'])
        
        out['conv3_1'] = F.relu(self.conv3_1(out['pool_2']))
        out['conv3_2'] = F.relu(self.conv3_2(out['conv3_1']))
        out['conv3_3'] = F.relu(self.conv3_3(out['conv3_2']))
        out['conv3_4'] = F.relu(self.conv3_4(out['conv3_3']))
        out['pool_3'] = self.pool_3(out['conv3_4'])
        
        out['conv4_1'] = F.relu(self.conv4_1(out['pool_3']))
        out['conv4_2'] = F.relu(self.conv4_2(out['conv4_1']))
        out['conv4_3'] = F.relu(self.conv4_3(out['conv4_2']))
        out['conv4_4'] = F.relu(self.conv4_4(out['conv4_3']))
        out['pool_4'] = self.pool_4(out['conv4_4'])
        
        out['conv5_1'] = F.relu(self.conv5_1(out['pool_4']))
        out['conv5_2'] = F.relu(self.conv5_2(out['conv5_1']))
        out['conv5_3'] = F.relu(self.conv5_3(out['conv5_2']))
        out['conv5_4'] = F.relu(self.conv5_4(out['conv5_3']))
        out['pool_5'] = self.pool_5(out['conv5_4'])

        return [out[layer] for layer in out_layers]


class GramMatrix(nn.Module):
    def forward(self, input):
        b, c, h, w = input.size()
        f = input.reshape(b, c, h*w) #BxCx(HxW)
        # torch.bmm
        # f: [BxCx(HxW)] @ [Bx(HxW)xC] -> [BxCxC]
        G = torch.bmm(f, f.transpose(1, 2))
        return G.div_(h*w)


class StyleLoss(nn.Module):
    def forward(self, input, target):
        GramInput = GramMatrix()(input)
        return nn.MSELoss()(GramInput, target)