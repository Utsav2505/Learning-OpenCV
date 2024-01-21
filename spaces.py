
#date-21 Jan,2023
import cv2 as cv

img =cv.imread('Photos/example.jpg');
cv.imshow('example',img);

#BGR to Grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)

cv.waitKey(0)