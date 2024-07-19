import cv2 as cv

# #reference the images
# img = cv.imread('Photos/landscape.jpg')
# #tell cv to show the image
# #notice how the large image will go off screen
# cv.imshow('Large landscape', img)
# #tell cv to wait till a key is pressed
# cv.waitKey(0)
#we will now show a video
capture = cv.VideoCapture('Videos/Shot 1.mp4')
#we read them frame by frame
while True:
    #get first frame
    isTrue, frame = capture.read()
    #show the frame
    cv.imshow('Vid',frame)
    #make the video stop if the letter d is pressed
    #the script will break with an error at the end
    #because the video ended
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
#release the devices
capture.release()
cv.destroyAllWindows()
