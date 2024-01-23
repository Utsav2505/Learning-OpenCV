#program to convert color channels
#date-21 Jan,2023
import cv2 as cv
import matplotlib.pyplot as plt

img =cv.imread('E:\Documents\Python\Open CV\Learning\Photos\example.JPG')
#matplotlib will show inverted color as opencv is  loading in BGR

# #BGR to RGB
# img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

#using matplotlib to read-display image
# cv.imshow('example',img)
# cv.waitKey(0)
# plt.imshow(img_rgb)
# plt.show()

# cv.imshow('example',img)
#openCV reads in BGR(Blue,Green,Red) format

# #BGR to Grayscale
# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow("gray",gray)

# #BGR to HSV(hue saturation value)
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("hsv",hsv)

# #BGR to L*A*B
# lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
# cv.imshow("lab",lab)


#HSV to BGR
bgr = cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow('bgr',bgr)
cv.waitKey(0)