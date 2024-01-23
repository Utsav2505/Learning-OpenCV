#program to split/merge color channels
#date-21 Jan,2023
import cv2 as cv
import numpy as np

# read a image and display normally
img =cv.imread('E:\Documents\Python\Open CV\Learning\Photos\example.JPG')
cv.imshow('img',img)


# splitted a image into 3 channels
b,g,r = cv.split(img);

# displayed all three channels
cv.imshow('b',b)
cv.imshow('g',g)
cv.imshow('r',r)

# printed all the dimensions of the channels
# in format (1080, 647, 3) : (x,y,colors)
print(img.shape)
# in foramat (1080, 647), here only one color so 1 is not displayed by default
print(b.shape)
print(g.shape)
print(r.shape)

# merged all three channels ans displayed 
merged = cv.merge([b,g,r])
cv.imshow('mege',merged)

# created a blank white area using numpy
blank = np.zeros(img.shape[:2],dtype='uint8')

# merged each color channel white blank white area
# so that every channel is visible 
# without doing so , each channels will be coloured brightest showing that channel intensity 
#  and will display on top of black color
bmerge = cv.merge([b,blank,blank])
gmerge = cv.merge([blank,g,blank])
rmerge = cv.merge([blank,blank,r])
cv.imshow('bmege',bmerge)
cv.imshow('gmege',rmerge)
cv.imshow('rmege',gmerge)


cv.waitKey(0)