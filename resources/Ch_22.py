# Face detection in images
import cv2 as cv

img = cv.imread('resources/inampic.jpg')

img = cv.resize(img, (500, 300))

cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows