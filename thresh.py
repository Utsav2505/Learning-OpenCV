#program to learn thresholding an image
# Thresholding the the binarisation of an image
# in this we convert an image to a binary image in which pixel will be either zero/black or 255/white
# we create a threshold value, if the pixel intensity is less than the value than we set the intensity to zero 
# if its higher than the value then we set it to 255
#date-30 Jan,2023
import cv2 as cv
import numpy as np

# read a image and display normally
img =cv.imread('E:\Documents\Python\Open CV\Learning\Photos\example.JPG')
cv.imshow('img',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

# simple thresholding
threshold,thresh = cv.threshold(gray,150,255,cv.THRESH_BINARY)
cv.imshow('simple threshold',thresh)

threshold,thresh_inv = cv.threshold(gray,150,255,cv.THRESH_BINARY_INV)
cv.imshow('simple threshold inverse',thresh_inv)

# Adaptive threshold
adaptive_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3)
cv.imshow('adaptive threshold',adaptive_thresh)

adaptive_thresh_inv = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY_INV,11,3)
cv.imshow('adaptive threshold inverse',adaptive_thresh_inv)

cv.waitKey(0)