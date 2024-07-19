import cv2 as cv

img = cv.imread('Photos/flowers.jpg')
cv.imshow('Flower', img)
# what is smoothing? we turn a single pixel into an average of its surrounding pixels
# for instance we can average each color intensitiy with the surrounding pixels
average = cv.blur(img, (3,3))
cv.imshow('Average Blur', average)

#gausian smoothing: a weighted average
# the weighted average. you get better results, more natural
gauss = cv.GaussianBlur(img, (3,3), sigmaX=0)
cv.imshow('Gaussian Blur', gauss)

#median blur: similar to average blurring, using median instead of average
#better at removing noise
median = cv.medianBlur(img, 11)
cv.imshow('Median Blur', median)

#bilateral blurring
#this is considered the most effective
#applies blurring, but retains edges
#the second argument is diameter of pixel neighborhood,
#third sigma color means that there are more colors to consider
#sigma space is the amount of pixels to consider in blur calculation
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral blur', bilateral)
#higher values may smudge images

cv.waitKey(0)