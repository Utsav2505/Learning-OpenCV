#Learning Contour detection using Open CV
#date- 2 Dec, 2023
import cv2 as cv
import numpy as np

#reading an image
img = cv.imread('Photos/example.JPG')

blank = np.zeros(img.shape, dtype= 'uint8')

#output/display image
cv.imshow('dew',img)

#converting this into grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('komigray',gray)

#blur
blur = cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT)

#Edge Cascade
canny=cv.Canny(blur,125,175)
#here 125,175 are the threshold values 1 & 2 respectively.
#to reduce the edges- use blur
cv.imshow('canny',canny)

ret,thresh = cv.threshold(gray,125,300,cv.THRESH_BINARY)
cv.imshow('threshhold',thresh)

#we can find contours by two methods- canny or threshold
#canny is prefferd do to more neat output

contours , hierarchies = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
#parameters of sindContours is image,mode,method, this funcn returns 2 things- contours , hierarchies
# here the contours will be containing the list of all the co-ordinates of the contours in the image after detecting the edges from canny
#RETR_LIST returns all the contours in the image, RETR_EXTERNAL returns the contours on the outside, RETR_TREE returns all the hierarchial contours 
#CHAIN_APPROX_SIMPLE method returns the simplest conntours that makes sense, CHAIN_APPROX_NONE does nothing extra and returns all te contours.
print(f'{len(contours)} contour(s) found!')

cv.drawContours(blank,contours,-1,(0,0,255),1)
cv.imshow('Drawn Contours',blank)

#waiting for 0ms
cv.waitKey(0)