# Converting video to grayscale and saving

import cv2 as cv
#from matplotlib.colors import is_color_like

cap = cv.VideoCapture('resources/Mulk.mp4')

# Writing format, coded, video writer object and file output
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv.VideoWriter('resources/Output_video.avi', cv.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (frame_width, frame_height), isColor= False)

while(True):
    (ret, frame) = cap.read()
    grayframe = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
   # (threshold, binary) = cv.threshold(grayframe, 127,255, cv.THRESH_BINARY)
# To show in player
    if ret == True:
        out.write(grayframe)
        cv.imshow('video', grayframe)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv.destroyAllWindows()