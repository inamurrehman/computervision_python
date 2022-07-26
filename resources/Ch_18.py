# How to change the perspective of an image

import cv2 as cv
import numpy as np

img = cv.imread('resources/PIC2.png')
print(img.shape)

# defining points
point1 = np.float32([[133, 96], [82, 71], [122, 69], [115, 82]])

width = 599
height = 350

widht, height = 599, 350

point2 = np.float32([[0,0], [width, 0], [0, height], [width, height]])

matrix = cv.getPerspectiveTransform(point1, point2)
out_img = cv.warpPerspective(img, matrix, (width, height))

# out_img = cv.resize

cv.imshow('Original ', img)
cv.imshow('Transformed', out_img)

cv.imwrite('resources/new.png', out_img)

cv.waitKey(0)
cv.destroyAllWindows()