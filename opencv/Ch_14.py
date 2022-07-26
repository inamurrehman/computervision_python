# How to draw lines and shapes in python Cv

import cv2 as cv
import numpy as np

# Draw a canvas, 0 is for Black and 1 is for white
img0 = np.zeros((600,600)) # Black
img1 = np.ones((600,600))  # White

# print size
print('The size of our canvas', img0.shape)
#print(img0) # print the matrix of the image

# Adding colors to the canvas

colored_img = np.zeros((600,600, 3), np.uint8 ) # color channel addition

colored_img[:] = 125,20,255 # To color complete image

colored_img[150:220, 10:200] = 125,220,0 # To color part of the image

# Adding line to the image
cv.line(colored_img, (120,70), (280,300), (0,50,130), 3) # part line
cv.line(colored_img, (400,500), (30,30), (50,50,0), 10) # cross line

cv.line(colored_img, (0,0), (colored_img.shape[1], colored_img.shape[0]), (250,0,30), 2) # cross line

# Adding rectangle
cv.rectangle(colored_img, (150,20), (200,200), (120,20,0), 3) # draw rectangel
cv.rectangle(colored_img, (250,170), (400,400), (120,120,0), cv.FILLED) # filled rectangel

# adding circle
cv.circle(colored_img, (200, 450), 60, (10,220,0), 3)

# Adding text
cv.putText(colored_img, 'This is my python program', (10,330), cv.FONT_HERSHEY_COMPLEX_SMALL, 1.5, (0,210,220))

#cv.imshow('Image with zeros (black)', img0)
#cv.imshow('Image with ones (white)', img1)
cv.imshow('Colored Image', colored_img)
cv.waitKey(0)
cv.destroyAllWindows()