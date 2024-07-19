import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("Photos/flowers.jpg")
cv.imshow('Flower', img)
#we will first compute the histogram for the grey scale img
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray Image', gray)

blank = np.zeros(img.shape[:2], dtype='uint8')
circle = cv.circle(blank, (img.shape[1]//2+500, img.shape[0]//2+300), 100, 255, -1)

mask = cv.bitwise_and(img, img, mask=circle)
cv.imshow('Mask', mask)

#compute gray histogram
#mask is if we only want the intensity in a specific area
#hist size is the number of bins we want in the histogram
#ranges is the range of pixel values
# gray_hist = cv.calcHist([gray], [0], mask=mask, histSize=[256], ranges=(0,256))

# plt.figure()
# plt.title('Gray scale histogram')
# plt.xlabel('Bins')
# plt.ylabel('Number of Pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()
# plt.clf()

#compute the histogram for a color image
plt.figure()
plt.title('Colors histogram')
plt.xlabel('Bins')
plt.ylabel('Number of Pixels')
colors = ('b','g','r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], mask=circle, histSize=[256], ranges=(0,256))
    plt.plot(hist, color=col)
    plt.xlim([0,256])
plt.show()

cv.waitKey(0)