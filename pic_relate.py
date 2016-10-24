import sys,os
import traceback
import cv2
def _is_real_pic(filename):
    try:
        ret=cv2.imread(filename)
        if ret is None: 
            return 0
        else:
            return 1
    except:
        return 0
    return 0
def del_pic_trash(mydir):
    for root,dirfile,filelist in os.walk(mydir):
        for fileone in filelist:
            file=os.path.join(root,fileone)
            if not _is_real_pic(file):
                os.remove(file)
def noisy(noise_typ,image):
    import cv2
    import numpy as np
    import random
    if noise_typ == "gauss":
        row,col,ch= image.shape
        mean = 0
        var = 0.1
        sigma = var**0.5
        gauss = np.random.normal(mean,sigma,(row,col,ch))
        gauss = gauss.reshape(row,col,ch)
        noisy = image + gauss
        return noisy
    elif noise_typ == "sp":
        row,col,ch = image.shape
        s_vs_p = 0.5
        amount = 0.004
        out = image
        # Salt mode
        num_salt = np.ceil(amount * image.size * s_vs_p)
        coords = [np.random.randint(0, i - 1, int(num_salt)) for i in image.shape]
        out[coords] = 1
        # Pepper mode
        num_pepper = np.ceil(amount* image.size * (1. - s_vs_p))
        coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in image.shape]
        out[coords] = 0
        return out
    elif noise_typ == "gus":
        gaussian_noise = image.copy()
        cv2.randn(gaussian_noise,128,30)
        out=gaussian_noise+image
        return out
    elif noise_typ == "gusblur":
        out=cv2.GaussianBlur(image,(5,5),1.5)
        return out
    elif noise_typ == "shuiyin":
        block=50
        shuiyin = np.ones((block,block,3),np.uint8)
        row,col,ch = image.shape
        hl=random.randint(0,row-block)
        wl=random.randint(0,col-block)
        image[hl:hl+block,wl:wl+block,:]=shuiyin
        return image
    else:
        return image

