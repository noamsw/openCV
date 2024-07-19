import cv2 as cv

#reference the images
img = cv.imread('Photos/landscape.jpg')
#tell cv to show the image
#notice how the large image will go off screen
cv.imshow('Large landscape', img)

#resizing for live video:
def changeRes(width, height):
    capture.set(3,width)
    capture.set(4,height)


#this function will rescale the image 
def rescaleFrame(frame, scale = 0.75):
    # resize the width and hight, converting to ints as expected
    height = int(frame.shape[0] * scale)
    width  = int(frame.shape[1] * scale)
    dimensions = (width, height)
    #resize the image
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

resized_image = rescaleFrame(img, 0.5)
cv.imshow("resized landscape", resized_image)

capture = cv.VideoCapture('Videos/Shot 1.mp4')
#we read them frame by frame
while True:
    #get first frame
    isTrue, frame = capture.read()
    #resize the frame
    resized_frame = rescaleFrame(frame)
    #show the frame
    cv.imshow('Vid',frame)
    cv.imshow('resized Vid',resized_frame)
    #make the video stop if the letter d is pressed
    #the script will break with an error at the end
    #because the video ended
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

#release the devices
capture.release()
cv.destroyAllWindows()