#learning transformations of image in openCV
#date-28 Nov 2023

import cv2 as cv
import numpy as np

img = cv.imread('Photos/example.jpg')
cv.imshow('komi',img)

#translations
def translate(img,x,y):
    transMat = np.float32([[1,0,x],[1,0,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)

#-x --> Left
#x --> Right
#-y --> Up
#y --> Down

translated = translate(img,2,2)
cv.imshow('translated',translated)

#rotations
def rotate(img,angle,origin=None):
    (height,width) = img.shape[:2]

    if origin is None:
        origin = (width//2,height//2)
    rotMat = cv.getRotationMatrix2D(origin,angle,1.0)
    dimensions = (width,height)

    return cv.warpAffine(img,rotMat,dimensions)

rotated = rotate(img,30)
cv.imshow('rotated',rotated)

#Resizing
resized = cv.resize(img,(500,500),interpolation=cv.INTER_AREA)
cv.imshow('resized',resized)

#Flipping
flipped = cv.flip(img,-1)
#parameteres- image,flipcode,
#flipcode, 0 : flipping at horizontal x axis, 1 : flipping vertical y axis, -1 : flipping both horizontally and vertically
cv.imshow('flipped',flipped)

#Cropping
cropped = img[50:200,200:500]
cv.imshow('crop',cropped)

cv.waitKey(0)