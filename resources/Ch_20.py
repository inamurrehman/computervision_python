# split video in to frames

import cv2 as cv
#import numpy as np

cap = cv.VideoCapture('resources/Cam_video.avi')
Nr = 0
while (True):
    success, frame = cap.read()
    if success:
        cv.imwrite(f"resources/frames/frame_{Nr}.jpg", frame)
        Nr = Nr + 1
    else:
        break
    
cap.release()