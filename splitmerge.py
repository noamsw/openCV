import cv2 as cv
import numpy as np

img = cv.imread('Photos/dog.jpg')
cv.imshow('Dog', img)

blue, green, red = cv.split(img)

# cv.imshow('Blue', blue)
# cv.imshow('Green', green)
# cv.imshow('Red', red)

#notice how the dimensions have changed to one channel
print(img.shape)
print(blue.shape)

#we can remerge the color channals
merged = cv.merge([blue,green, red])
# cv.imshow('Merged', merged)

#show the colors themselves, not in grey
#make a blank img
blank = np.zeros(img.shape[:2], dtype='uint8')
#lets print only green
b = cv.merge([blue, blank, blank])
g = cv.merge([blank, green, blank])
r = cv.merge([blank, blank, red])

cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)

cv.waitKey(0)