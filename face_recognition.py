import cv2 as cv
import numpy as np
import os

haar_cascade = cv.CascadeClassifier('haar_face.xml')
people = []
for folder in os.listdir(r'C:\Users\noams\Documents\Projects\python\computerVision\openCV\Faces\val'):
    people.append(folder)
face_recognizer = cv.face.LBPHFaceRecognizer.create()
face_recognizer.read('trained_face_model.yml')
DIR = r'C:\Users\noams\Documents\Projects\python\computerVision\openCV\Faces\val'

def computeAccuracy():
    true = 0
    false = 0
    for person in people:
            path = os.path.join(DIR, person)
            true_label = person

            for img in os.listdir(path):
                img_path = os.path.join(path, img)

                img_array = cv.imread(img_path)
                gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
                face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
                for (x,y,w,h) in face_rect:
                    face_roi = gray[y:y+h, x:x+w]
                    pred_label, confidence_level = face_recognizer.predict(face_roi)
                    if people[pred_label] == true_label:
                        true+=1
                    else:
                        false+=1
                        cv.putText(img_array, str(people[pred_label]), (20,20), cv.FONT_HERSHEY_COMPLEX, fontScale=0.5, color=(0,255,0), thickness=2)
                        cv.rectangle(img_array, (x,y), (x+w,y+h), (0,255,0), thickness=2)
                        cv.imshow(f'{img_path}', img_array)
    print(f'Accuracy: {true / (true + false)}')
            
computeAccuracy()
# img = cv.imread(r'C:\Users\noams\Documents\Projects\python\computerVision\openCV\Faces\val\elton_john\1.jpg')
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Unidentified Person', gray)

# faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
# for (x,y,w,h) in faces_rect:
#     face_roi = gray[y:y+h, x:x+w]
#     #perform face recognition
#     label, confidence_level = face_recognizer.predict(face_roi)
#     print(f'label: {people[label]}, confidence level: {confidence_level}')
#     cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, fontScale=0.5, color=(0,255,0), thickness=2)
#     cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)
# cv.imshow('Recognized face', img)
cv.waitKey(0)