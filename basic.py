import cv2 as cv

img = cv.imread('Photos/lana.jpg')
cv.imshow('Lana', img)

#converting the image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grey', gray)

#blurring an image, i.e. removing noise, using gausian blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

#edge cascade, i.e. finding the edges using the canny edge detector
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny', canny)
blurred_canny = cv.Canny(blur, 125, 175)
cv.imshow('Blurred Canny', blurred_canny)

#dilating the image, using the edges
dilated = cv.dilate(canny, (3,3), iterations=3)
cv.imshow('Dilated', dilated)

#eroding the dilation, i.e. reverting the dilation
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('Eroded', eroded)

#Resizing an image
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

#cropping
cropped = resized[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)