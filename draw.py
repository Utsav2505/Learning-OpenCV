import cv2 as cv
import numpy as np

# there are 2 ways to draw- draw on an existing image or draw on a dummy image  

# to create a dummy blank image of 500x500 with 3 channels of color of data type uint8 which is for an image.
blank=np.zeros((500,500,3),dtype='uint8') 

#1.Paint the image with a certain color
#blank[:]=0,255,0 #selecting all the pixels of the canvas and setting its color to green
#or select a certain portion
blank[200:300,300:400]=0,255,0

#2.Draw a rectangle
cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=2)
#parameters(img,pt1,pt2,color,thickness=None,lineType=None,shift=None,/)
#use thickness=cv.FILLED or as '-1' to fill the rectangle

#3.draw a circle
cv.circle(blank,(250,250),40,(0,0,255),thickness=4)
cv.imshow('circle',blank)

#4. Draw a line
cv.line(blank,(250,250),(0,0),(255,0,0),thickness=5)
cv.imshow('line',blank)

#5.Text on an Image
cv.putText(blank,"Hello",(250,250),cv.FONT_HERSHEY_TRIPLEX,1.0,(255,255,255),thickness=2)
cv.imshow('text',blank)

cv.imshow('canvas',blank)

cv.waitKey(0)
