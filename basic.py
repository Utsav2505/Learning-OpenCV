#learning basic functions of openCV
#date-28 Nov 2023

import cv2 as cv

img = cv.imread('Photos/example.jpg')
cv.imshow('komi',img)


#converting image to grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('komigray',gray)

#blur
blur = cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
#here (3,3) is the kernel size

#Edge Cascade
canny=cv.Canny(blur,125,175)
#here 125,175 are the threshold values 1 & 2 respectively.
#to reduce the edges- use blur
cv.imshow('canny',canny)

#Dilating the image
dilated=cv.dilate(canny,(7,7),iterations=3)
#here canny is used as a structure(edges), (3,3) are kernel size,
cv.imshow('dilated',dilated)

#Eroding the dilated image
eroded=cv.erode(dilated,(7,7),iterations=3)
cv.imshow('eroded',eroded)
#we can erode the dilated image to get back the canny/edge image

#Resize
resized = cv.resize(img,(500,500),interpolation=cv.INTER_AREA)
cv.imshow('resized',resized)
#this method resizes the images, ignoring the aspect ratio
#interpolation gives much better quality - INTER_AREA < LINEAR < CUBIC
resized2 = cv.resize(img,(500,500))
cv.imshow('resized2',resized2)

#Cropping
cropped = img[50:200,200:500]
cv.imshow('crop',cropped)

#output/display image
cv.imshow('komiblur',blur)


#waiting for 0ms
cv.waitKey(0)