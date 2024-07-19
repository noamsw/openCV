import cv2 as cv
import numpy as np


img = cv.imread('Photos/dog.jpg')
blank = np.zeros(img.shape, dtype='uint8')

#convert the image to greyscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# #blur the image before
blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
# get ganny edges
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny', canny)

#another option:
# ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# cv.imshow('Threshold', thresh)
#get contours
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
#the contours looks at the structure and returns the contours and hierarchies. 
# chain approx returns all the contours. simple will return the most simple one
print(f'number of contours: {len(contours)}')

cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Drawn counters', blank)
cv.waitKey(0)