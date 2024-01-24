#program to learn masking
#date-24 Jan,2023
import cv2 as cv
import numpy as np

# read a image and display normally
img =cv.imread('E:\Documents\Python\Open CV\Learning\Photos\example.JPG')
cv.imshow('img',img)

# creating a blank area 
blank = np.zeros(img.shape[:2],dtype='uint8')
# the size of this blank(mask) must be same of the image size otherwise it will not work

# creating a mask using circle(rect also can be used)  
mask = cv.circle(blank,(img.shape[1]//2,img.shape[0]//2-300),150,255,-1)
cv.imshow('mask',mask)

# applying bitwise operations on the image and the mask 
masked = cv.bitwise_and(img,img,mask=mask)
cv.imshow('masked',masked)
cv.waitKey(0)
