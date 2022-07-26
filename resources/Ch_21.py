# How to detect specific colors from video in python

import cv2 as cv
import numpy as np

#img = cv.imread('resources/inampic.jpg')

# converting to HSV
#hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# Sliders
def slider():
    pass

path = 'resources/inampic.jpg'

cv.namedWindow('Bars')
cv.resizeWindow('Bars', 600, 400)

cv.createTrackbar('hue min', 'Bars', 0, 179, slider)
cv.createTrackbar('hue max', 'Bars', 179, 179, slider)
cv.createTrackbar('sat min', 'Bars', 0, 255, slider)
cv.createTrackbar('sat max', 'Bars', 255, 255, slider)
cv.createTrackbar('val min', 'Bars', 0, 255, slider)
cv.createTrackbar('val max', 'Bars', 255, 255, slider)

while True:
    img = cv.imread(path)
    hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    hue_min = cv.getTrackbarPos('hue min', 'Bars')
    hue_max = cv.getTrackbarPos('hue max', 'Bars')
    sat_min = cv.getTrackbarPos('sat min', 'Bars')
    sat_max = cv.getTrackbarPos('sat max', 'Bars')
    val_min = cv.getTrackbarPos('val min', 'Bars')
    val_max = cv.getTrackbarPos('val max', 'Bars')
    print(hue_min, hue_max, sat_min, sat_max, val_min, val_max)

    # To see the changes inside the image
    lower = np.array([hue_min, sat_min, val_min])
    upper = np.array([hue_max, sat_max, val_max])
    mask_img = cv.inRange(hsv_img, lower, upper)
    out_img = cv.bitwise_and(img, img, mask = mask_img)
   
    cv.imshow('Original', img)
    cv.imshow('HSV image', hsv_img)
    cv.imshow('mask image', mask_img)
    cv.imshow('output image', out_img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cv.destroyAllWindows()

