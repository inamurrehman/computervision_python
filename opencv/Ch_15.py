# Resolution of Cam
import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

# Resolution (1280, 720)
#cap.set(3, 1280) # simply
#cap.set(4, 720)

def hd_resolution(): # using function
    cap.set(3, 1280)
    cap.set(4, 720)
def fhd_resolution(): # using function
    cap.set(3, 1920)
    cap.set(4, 1080)
def fps():
    cap.set(cv.CAP_PROP_FPS, 30) # FPS setting
    print('fps', cap.get(cv.CAP_PROP_FPS))

#hd_resolution()
fhd_resolution()
# Frames per second
fps()

while(True):
    ret, frame = cap.read()
    if ret == True:
        cv.imshow('Camera', frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv.destroyAllWindows()