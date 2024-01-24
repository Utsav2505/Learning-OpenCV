#program to learn histogram
#date-24 Jan,2023
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt 

# read a image and display normally
img =cv.imread('E:\Documents\Python\Open CV\Learning\Photos\example.JPG')
cv.imshow('img',img)

##### Creating a grayscale histogram #####

# creating a mask
blank = np.zeros(img.shape[:2],dtype='uint8')

# converting image to grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#cv.imshow('gray',gray)

# created a mask shape
circle = cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)
mask = cv.bitwise_and(gray,gray,mask=circle)
cv.imshow('mask',mask)

# grayscale histogram
# format: ([sequence of images],[sequence of channels(using 0 as it is grayscale)]
# ,mask shape,histsize(no. of bins to be used while calculating histogram),range of pixels where we are calculating hist)
# we can use either a masked image or set as none
hist = cv.calcHist([gray],[0],mask,[256],[0,256])
plt.figure()
plt.title('masked Grayscale Histogram')
plt.xlabel('bins')
plt.ylabel('# of pixels')
plt.plot(hist)
plt.xlim([0,256])
plt.show()
# in x axis it is intensity and y axis is the no. of pixels
# so this histo shows the population of pixels at a specific intensity

#####Creating a color Histogram
# creating a mask
blank2 = np.zeros(img.shape[:2],dtype='uint8')

# created a mask shape
mask2 = cv.circle(blank2,(img.shape[1]//2,img.shape[0]//2),100,255,-1)
masked2 = cv.bitwise_and(img,img,mask=mask2)
cv.imshow('mask2',masked2)

# created a tuple to hold the values of colors
colors = ('b','g','r')

plt.figure()
plt.title('Color Histogram')
plt.xlabel('bins')
plt.ylabel('# of pixels')


for i,col in enumerate(colors):
    hist = cv.calcHist([img],[i],mask2,[256],[0,256])
    plt.plot(hist,color = col)
    plt.xlim([0,256])
plt.show()    

cv.waitkey(0)