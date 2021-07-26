# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 16:11:44 2021

@author: Toshıba
"""

import cv2 as cv
from matplotlib import pyplot as plt

resim= cv.imread("kulaklik.jpg",0)
cv.namedWindow("resim",cv.WINDOW_NORMAL)
cv.imshow("resim",resim)
cv.imshow("resim penceresi",resim)

plt.imshow(resim,cmap="gray")
plt.show()

k=cv.waitKey(0)
    
if k==ord("q"):
    print("q tusuna basildi, resim kayit edildi")
    cv.imwrite("kulaklik.jpg",resim)
    
cv.destroyAllWindows()