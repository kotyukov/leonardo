import torch
import torchvision.transforms as transforms
import torch.nn as nn
import torchvision.utils as tutils
from model import VGG_nst, GramMatrix, StyleLoss
from PIL import Image

def run_style_transfer(model, optim_img, optimizer, iter_num, loss_layers, targets, loss_funcs, weights):
    for iteration in range(iter_num):
        def closure():
            optimizer.zero_grad()
            out = model(optim_img, loss_layers)
            
            totalLossList = []
            for i in range(len(out)):
                criterion = loss_funcs[i]
                output = out[i]
                target = targets[i]
                weight = weights[i]
                loss = criterion(output, target) * weight
                totalLossList.append(loss)
            total_loss = sum(totalLossList)
            total_loss.backward()
            return total_loss
        optimizer.step(closure)

    res_img = postprocess(optim_img.data[0].cpu().squeeze())
    return res_img


def preprocess(img, size):
    img = transforms.Resize(size)(img)
    img = transforms.ToTensor()(img)
    img = transforms.Lambda(lambda x:x[torch.LongTensor([2, 1, 0])])(img) #RGB to BGR
    img = transforms.Normalize(mean=[0.407, 0.458, 0.485], std=[1, 1, 1])(img) #imagenet mean
    img = transforms.Lambda(lambda x: x.mul_(255))(img)
    return img


def postprocess(img):
    img = transforms.Lambda(lambda x: x.mul_(1./255))(img)
    img = transforms.Normalize(mean=[-0.407, -0.458, -0.485], std=[1,1,1])(img)
    img = transforms.Lambda(lambda x: x[torch.LongTensor([2, 1, 0])])(img) #turn to RGB
    img = img.clamp_(0,1)
    return img


def get_model(path_to_pretrained, pooling='avg'):
    if pooling != 'avg' and pooling != 'max':
        raise BaseException("Неправильно указан pooling-тип. " +
                            "Допустимые значения: avg, max.")
    model = VGG_nst(pooling)
    model.load_state_dict(torch.load(path_to_pretrained))
    for param in model.parameters():
        param.requires_grad = False
    return model


def get_loss_funcs(style_layers, content_layers):
    style_losses = [StyleLoss()] * len(style_layers)
    content_losses = [nn.MSELoss()] * len(content_layers)
    funcs = style_losses + content_losses
    return funcs


def get_targets(model, style_layers, content_layers, style_images, content_image):
    style_targets = []
    for img, weight in style_images:
        style_targets.append([GramMatrix()(t).detach() * weight for t in model(img, style_layers)])
    style_targets = [sum(t) for t in zip(*style_targets)]
    content_targets = [t.detach() for t in model(content_image, content_layers)]
    targets = style_targets + content_targets
    return targets


def normalize_weights(styles_dict):
    total = sum(styles_dict.values())
    for k, v in styles_dict.items():
        styles_dict[k] = float(v)/total


def load_img(path, img_size):
    img = Image.open(path)
    img = preprocess(img, img_size)
    img = img.unsqueeze(0)
    return img


def save_img(img):
    tutils.save_image(img, 'result.png', normalize=True)
    return