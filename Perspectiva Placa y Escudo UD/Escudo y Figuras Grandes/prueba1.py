# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 19:52:45 2015

@author: Jorge Ulises Useche Cuellar
"""
import matplotlib.pyplot as plt
import matplotlib.image as Image
import numpy as np
fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, figsize=(6,10))

im1 = Image.imread("escudo_ud_rainbow_byn.png")
ax1.imshow(im1)
im2 = Image.imread("escudo_ud_rainbow.png")
ax2.imshow(im2)
fig, plt.imshow(im2)
#plt.show()