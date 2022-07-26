# Joining two images

import cv2 as cv
import numpy as np

img = cv.imread('resources/inampic.jpg')
img1 = cv.imread('resources/Image_gray.jpg')
# Stacking an image

#1  horizontal stack

hor_img = np.hstack((img, img))

# 2 Vertical stack

ver_img = np.vstack((img1, img1))

cv.imshow('Horizontal imges', hor_img)
cv.imshow('Vertical imges', ver_img)
cv.waitKey(0)
cv.destroyAllWindows()

# You can stack images with same shape (width, height, color channel)
# We can not resize the stack image ( it need a function)
# Same number of channels is needed for usin np function
# (600,500,3)