# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 22:25:48 2021

@author: Toshıba
"""

import cv2

cam = cv2.VideoCapture(0)

fourrc = cv2.VideoWriter_fourcc(*'XVID')

out = cv2.VideoWriter("video.avi",fourrc, 30.0,(640,480))

while cam.isOpened():
    
    ret, frame = cam.read()
    
    if not ret:
        print("kameradan görüntü alınamadı")
        break
    
    out.write(frame)
    
    cv2.imshow("kamera",frame)
    
    if cv2.waitKey(33) == ord("q"):
        print("videodan ayrıldınız.")
        break


cam.release()
out.release()
cv2.destroyAllWindows()