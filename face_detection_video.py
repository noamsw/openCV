import cv2 as cv

# define a video capture object 
vid = cv.VideoCapture(0) 
haar_cascade = cv.CascadeClassifier('haar_face.xml')

while(True): 
     
    # Capture the video frame 
    ret, frame = vid.read() 
    face_rect = haar_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=6)

    for (x,y,w,h) in face_rect:
        cv.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), thickness=2)

    # Display the resulting frame 
    cv.imshow('frame', frame) 
      
    #use q to quit
    if cv.waitKey(1) & 0xFF == ord('q'): 
        break
  
# After the loop release the cap object 
vid.release() 
# Destroy all the windows 
cv.destroyAllWindows() 