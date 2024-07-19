import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Photos/dog.jpg')
cv.imshow('Dog', img)

#BGR to Grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

#BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow('HSV', hsv)

#BGR to LAb
lab = cv.cvtColor(img, cv.COLOR_BGR2Lab)
cv.imshow('LAB', lab)

#openCV uses BGR, opposite of more common RGB
#the image colors will be inverted
# plt.imshow(img)
# plt.show()

# BGR to RGB
# rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# cv.imshow('RGB', rgb)
# # now matplotli will work
# plt.imshow(rgb)
# plt.show()

# #inverse of what we have seen:
# #convert gray to BGR, HSV to BGR
# hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
# cv.imshow('HSV to BGR', hsv_bgr)
# LAB to BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('LAB to BGR', lab_bgr)

#note that converting gray directly to LAB/HVS does not exist
#first convert to BGR
cv.waitKey(0)