import cv2 as cv
import numpy as np

img = cv.imread('Photos/dog.jpg')
cv.imshow('Flowers', img)

#we have seen canny edge detector
#now lets see laplacian
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

#sobel gradient magnitude representation
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)
combined = cv.bitwise_or(sobelx, sobely)
cv.imshow('Combined Sobel', combined)

#canny edge
canny = cv.Canny(gray, 100, 150)
cv.imshow('Canny edge', canny)


cv.waitKey(0)