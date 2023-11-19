#Program to read-resize-display images using OpenCV
#date-19 Nov,2023
import cv2 as cv

#creating a function to rescale the frames of the video
def rescaleFrame(frame,scale = 0.6):
    width = int (frame.shape[1]*scale) # shape is a A tuple representing the dimensions of the frame in the format (height, width, channels)
    height = int (frame.shape[0]*scale)

    dimensions = (width,height) #creating a new tuple
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA) #interpolation=cv.INTER_AREA argument specifies the interpolation method to be used during resizing (in this case, INTER_AREA).

#input-read the image
img = cv.imread('Photos/photo.JPG')
#resize image
resize_img=rescaleFrame(img,scale=0.2)
#output/display image
cv.imshow('dew',resize_img)
#waiting for 0ms
cv.waitKey(0)