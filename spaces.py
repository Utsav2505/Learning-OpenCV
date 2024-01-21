
#date-21 Jan,2023
import cv2 as cv
import matplotlib.pylot as plt

img =cv.imread('Photos/example.jpg');
cv.imshow('example',img);
#openCV reads in BGR(Blue,Green,Red) format

#BGR to Grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)

#BGR to HSV(hue saturation value)
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("hsv",hsv)

#BGR to L*A*B
lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow("lab",lab)

#using matplotlib to read-display image
plt.imshow(img)
plt.show()
cv.waitKey(0)