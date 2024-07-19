import cv2 as cv
import numpy as np

img = cv.imread('Photos/flowers.jpg')
cv.imshow('Flower', img)
#masking allows us to focus only on certain areas
#masks must be the same size as your image
blank = np.zeros(img.shape[:2], dtype='uint8')

circle = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow('Circle', circle)

rectangle = cv.rectangle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), (blank.shape[0]//2 + 100, blank.shape[1]//2 + 100), 255, -1)
cv.imshow('Rectangle', rectangle)

mask = cv.bitwise_and(rectangle, circle)
cv.imshow('Mask', mask)

masked = cv.bitwise_and(img,img, mask=mask)
cv.imshow('Masked Image', masked)
cv.waitKey(0)