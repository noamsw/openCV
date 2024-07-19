import cv2 as cv

img = cv.imread('Photos/flowers.jpg')
cv.imshow('FLowers', img)
#thresholing is a binarizatino of an image
#turning pixels either on or off
#the simplest way is to take a threshold value, and turn off all pixels below this value

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#simple thresholding
threshold, thresh = cv.threshold(gray, 100, 255, cv.THRESH_BINARY)
cv.imshow('Simple Binarized threshold', thresh)
#create an inverse thresholded image
threshold, thresh_inverse = cv.threshold(gray, 100, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Binarized threshold inverted', thresh_inverse)
#adaptive thresholding, waht happens when we dont want to set the threshold?
#let the program the optimal threshold
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('Adaptive thresholding', adaptive_thresh)

cv.waitKey(0)