#program to smooth out images/ apply blur
#date-24 Jan,2023
import cv2 as cv
import numpy as np

# read a image and display normally
img =cv.imread('E:\Documents\Python\Open CV\Learning\Photos\example.JPG')
cv.imshow('img',img)

#Averaging
# In this method a window(martix) created,
# in which the pixel intensity of the middle pixel 
# is the average of all the surrounding intensity of pixels
# here 3,3 is the kernel size
average = cv.blur(img,(3,3))
cv.imshow('avg',average)

# Gaussian Blur
# In this method, instead of averaging the intensities as done above
# here weights are assigned to surrounding pixels
# and the centre pixel weight is the average of all teh weights of surroundings
# here zero represents the sigmaX which means the standard deviation in X direction
gaussian = cv.GaussianBlur(img,(3,3),0)
cv.imshow('gauss',gaussian)
# gaussian is better than averaging cauz its more natural
# gaussian has low blur than averaging

# Median Blur
# Its similar to average but the differenece is that 
# Centre pixel is the median of  the surrounding pixels
# here only single integer(let it x) is passed instead of tuple
# as the function will automatically assume it to be (x,x)  
# kernal size is taken small in case of median
median = cv.medianBlur(img,3)
cv.imshow('median',median)

# Bilateral blur
# this method applies blurring but retains the edges of the image
# format - (source imag, diameter , Sigmacolor , sigmaspace)
bilateral = cv.bilateralFilter(img,5,15,15)
cv.imshow('bilateral',bilateral)
cv.waitKey(0)