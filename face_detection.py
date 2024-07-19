import cv2 as cv

img = cv.imread('Photos/people.jpg')
# cv.imshow('People', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray People', gray)
#initialize a haar classifier
#we will use classifers to decide whether a face is present or not
#classifiers need to be pretrained
#opencv has these
#we will use haar cascades
#local binary patterns are a more advanced version
haar_cascade = cv.CascadeClassifier('haar_face.xml')

face_rect = haar_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=6)
print(f'number of faces found: {len(face_rect)}')

for (x,y,w,h) in face_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)

cv.imshow('Detected faces', img)
#remeber that many times open cacades will have false positive
cv.waitKey(0)