# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 23:22:05 2021

@author: Toshıba
"""

import cv2
import numpy as np

img=np.zeros((512,512,3),np.uint8)
cv2.line(img,(0,0),(511,511),(255,0,0),5)
cv2.line(img,(50,400),(400,50),(0,255,0),10)

cv2.rectangle(img,(50,50),(300,300),(0,0,255),-1)

cv2.circle(img,(255,255),60,(120,120,120),2)

cv2.ellipse(img,(256,256),(100,50),0,0,180,(255,100,0),2)

pts=np.array([[20,30],[100,120],[255,255],[10,400]],np.int32)
pts2=pts.reshape(-1,1,2)
cv2.polylines(img,[pts],True,(255,255,255),3)

font=cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img,'OpenCv',(10,400),font,4,(0,155,255),2,cv2.LINE_AA)
cv2.imshow("resim",img)
cv2.waitKey(0)
cv2.destroyAllWindows()