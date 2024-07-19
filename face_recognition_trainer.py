import cv2 as cv
import os
import numpy as np
# we will reocgnize faces using openCVs face recognizer
# we will use openCV built in model
people = []
for folder in os.listdir(r'C:\Users\noams\Documents\Projects\python\computerVision\openCV\Faces\train'):
    people.append(folder)
DIR = r'C:\Users\noams\Documents\Projects\python\computerVision\openCV\Faces\train'
haar_cascade = cv.CascadeClassifier('haar_face.xml')
features = []
labels = []

def createTrain():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
            for (x,y,w,h) in face_rect:
                face_roi = gray[y:y+h, x:x+w]
                features.append(face_roi)
                labels.append(label)
createTrain()
#convert features and labels for lbph recognizer
features = np.array(features, dtype='object')
labels = np.array(labels)
#train the recognizer on the faces
face_rocognizer = cv.face.LBPHFaceRecognizer.create()
face_rocognizer.train(features, labels)
np.save('features.npy', features)
np.save('labels.npy', labels)
#we want to save the trained model
face_rocognizer.save('trained_face_model.yml')