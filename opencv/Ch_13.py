# Basic functions or manipulations in opencv

import cv2 as cv
from cv2 import cvtColor
import numpy as np

img= cv.imread('resources/inampic.jpg')
 
# Resize
resized_img = cv.resize(img, (450,250))

# Gray image
gray_img = cvtColor(img, cv.COLOR_BGR2GRAY)

# Blurred Image
blurr_img = cv.GaussianBlur(img, (27,27), 0)

# Edge detection

edge_img = cv.Canny(img, 57,57)

# Thickness of lines 
dialated1_img = cv.dilate(edge_img, (3,3), iterations= 1)
# editing thikness of lines
mat_kernel = np.ones((3,3), np.uint8)
dialated2_img = cv.dilate(edge_img, (mat_kernel), iterations= 1)

# Erosion or thinner outlines
ero_img = cv.erode(dialated2_img, mat_kernel, iterations= 1)

# Cropping, we will use numpy library
print('The size of the image is:', img.shape)
cropped_img = img[30:220, 0:230]

cv.imshow('Original Image', img)
cv.imshow('Resized Image', resized_img)
cv.imshow('Gray Image', gray_img)
cv.imshow('Blurred Image', blurr_img)
cv.imshow('Edge Image', edge_img)
cv.imshow('Dilated1 Image', dialated1_img)
cv.imshow('Dilated2 Image', dialated2_img)
cv.imshow('Erosion Image', ero_img)
cv.imshow('Cropped Image', cropped_img)

cv.waitKey(0)
cv.destroyAllWindows()
