import cv2 as cv
import numpy as np
#there are 4 major bitwise operators
#AND, OR, XOR, NOT
#these are used many times for masks
blank = np.zeros((400,400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (blank.shape[0]//2, blank.shape[1]//2),  200, 255, -1)
cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)

#bitwise AND. otherwise known as intersection
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('Bitwise And', bitwise_and)

#bitwise OR. shows the non intersection areas and intersectiion areas
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('Bitwise OR', bitwise_or)

#bitwise XOR, shows non intersection regions
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('Bitwise Xor', bitwise_xor)

#bitwise NOT
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow('Bitwise Rectangle Not', bitwise_not)

cv.waitKey(0)