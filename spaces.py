
#date-21 Jan,2023
import cv2 as cv
import matplotlib.pyplot as plt

img =cv.imread('Photos/example.jpg');
img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

cv.imshow('example',img)
cv.waitKey(0)
plt.imshow(img_rgb)
plt.show()
# cv.imshow('example',img)
#openCV reads in BGR(Blue,Green,Red) format

# #BGR to Grayscale
# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow("gray",gray)

# #BGR to HSV(hue saturation value)
# hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
# cv.imshow("hsv",hsv)

# #BGR to L*A*B
# lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
# cv.imshow("lab",lab)

#using matplotlib to read-display image

# cv.waitKey(0)