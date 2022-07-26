# Writing videos from Cam

import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

# Writing format, coded, video writer object and file output
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv.VideoWriter('resources/Cam_video.avi', cv.VideoWriter_fourcc('M', 'J', 'P', 'G'), 20, (frame_width, frame_height))

while(True):
    (ret, frame) = cap.read()
    #grayframe = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
   # (threshold, binary) = cv.threshold(grayframe, 127,255, cv.THRESH_BINARY)
# To show in player
    if ret == True:
        out.write(frame)
        cv.imshow('video', frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv.destroyAllWindows()