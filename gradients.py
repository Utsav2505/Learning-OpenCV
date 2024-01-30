#program to learn edge detection/gradient
#date-30 Jan,2023
import cv2 as cv
import numpy as np

# read a image and display normally
img =cv.imread('E:\Documents\Python\Open CV\Learning\Photos\example.JPG')
cv.imshow('img',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

# Laplacian method
lap = cv.Laplacian(gray,cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('laplacian',lap)

# Sobel Method
sobel_x = cv.Sobel(gray,cv.CV_64F,1,0)
sobel_y = cv.Sobel(gray,cv.CV_64F,0,1)
combined = cv.bitwise_or(sobel_x,sobel_y)
cv.imshow('sobelx',sobel_x)
cv.imshow('sobely',sobel_y)
cv.imshow('combine sobel',combined)

# canny
canny = cv.Canny(gray,150,175)
cv.imshow('canny',canny)

cv.waitKey(0)