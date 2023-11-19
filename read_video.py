#program to read-resize-display a video using openCV
#date-Nov 19,2023
import cv2 as cv

#creating a function to rescale the frames of the video
#will work for images, video, livecapture
def rescaleFrame(frame,scale = 0.6):
    width = int (frame.shape[1]*scale) # shape is a A tuple representing the dimensions of the frame in the format (height, width, channels)
    height = int (frame.shape[0]*scale)

    dimensions = (width,height) #creating a new tuple
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA) #interpolation=cv.INTER_AREA argument specifies the interpolation method to be used during resizing (in this case, INTER_AREA).

#creating a function to change resolution
def changeRes(width,height):
    #will only work for live capture
    capture.set(3,width)
    capture.set(4,height)
    #we can use this function in place of rescale frame for changing resolution of live capture 

#Input video
capture = cv.VideoCapture('Videos/video.mp4')#use an integer(0,1,2,3) to select a webcam/camera in place of the path for live capture.

#using while loop to read video frame by frame and displaying
while True:
    isTrue, frame = capture.read() #'isTrue-Confirming that frame is sucessfully read
    frame_resize = rescaleFrame(frame) #resizing frame
    cv.imshow('video',frame_resize) #output the resized frames
    if cv.waitKey(20) & 0xFF==ord('d'): #the while loop will continue to run until 20milliseconds have passed and d key is pressed on keyboard
        break

capture.release() # realeasing the input taken to free up system resources
cv.destroyAllWindows() #closing the output window

