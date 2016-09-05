# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 19:52:45 2015

@author: Jorge Ulises Useche Cuellar
"""
from numpy import *
from matplotlib.pyplot import *
#import matplotlib.pyplot as plt
#import matplotlib.image as Image
#from sympy import *
from PIL import Image
#import numpy as np
#fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, figsize=(6,10))
#ax1.imshow(im1)
#ax2.imshow(im2)
#ax3.imshow(grid, extent=[0,100,0,1], aspect=100)
#ax3.set_title('Manually Set Aspect')
#plt.tight_layout()
#plt.show()

#TRANSFORMACIÓN GEOMÉTRICA BILINEAL

im1 = imread('placasdelamadre.png')
y = array([1,1,160,160])
x = array([1,330,330,1])
yp = array([63,20,132,252])
xp = array([84,295,310,129])

Mp = array([xp,yp,xp*yp,ones(4,1)])
ap = Mp^(-1)*x;
bp = Mp^(-1)*y;

im2=uint8(zeros(288,384))
for m in range(1,288):
    for n in range(1,384):
        yt = round(bp*[n,m,n*m,1]);
        xt = round(ap*[n,m,n*m,1]);
        if yt>=1 and yt<=160 and xt>=1 and xt<=330:
            im2[m,n]=im1(yt,xt)
        else:
            im2[m,n]=uint8(0)
figure, imshow(im2);



#im1 = Image.open("escudo_ud_rainbow_byn.png")
#imshow(im1)
#Z=np.array(((1,2,3,4,5),(4,5,6,7,8),(7,8,9,10,11)))