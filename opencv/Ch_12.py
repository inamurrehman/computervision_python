# Setting of camera or video

import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
cap.set(10, 50) # 10 for brightness setting
cap.set(3, 640) # width
cap.set(4, 480) # Height
while(True):
    ret, frame = cap.read()
    if ret == True:
        cv.imshow('Frame', frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv.destroyAllWindows()
