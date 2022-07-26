# Coordinates of an image

# Step 1 Import libraries

import cv2 as cv
import numpy as np

# step 2 Define a function

def find_coord(event, x, y, flages, params):
    if event == cv.EVENT_LBUTTONDOWN:
        # Left button down
        print(x,'', y)
        # how to define or print on the same image or window
        font = cv.FONT_HERSHEY_PLAIN
        cv.putText(img, str(x) + ',' + str(y), (x,y), font, 1, (255,0,0), thickness= 2)
        # Show the text on image and img itself
        cv.imshow('image', img)

# Final function to read a display
if __name__ == '__main__':
    # reading an image
    img = cv.imread('resources/inampic.jpg', 1)
    # display the image
    cv.imshow('image', img)
    # settting call back function
    cv.setMouseCallback('image', find_coord)

    cv.waitKey(0)
    cv.destroyAllWindows()