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


cv.waitkey(0)