#program to learn bitwise operations in openCV
#date-24 Jan,2023
import cv2 as cv
import numpy as np

# Create a blank image and draw a circle and a rectangle on it 
blank = np.zeros((400,400),dtype='uint8')
circle= cv.circle(blank.copy(),(200,200),200,255,-1)
rectangle = cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
# used acopy of blank to kept them separate
cv.imshow('circle',circle)
cv.imshow('rect',rectangle)

# Bitwise AND
# here we can see that we are getting an intersection area of both circle and rectangle
bitwise_and = cv.bitwise_and(circle,rectangle)
cv.imshow('AND',bitwise_and)

# Bitwise OR
# here we can see that we are getting the union of both these shapes
bitwise_or = cv.bitwise_or(circle,rectangle)
cv.imshow('OR',bitwise_or)

# Bitwise XOR
# here we can see that we are getting a area which is uncommon in bothe shapes
# or we can say that it is the subtraction of regions in OR and AND: (OR-AND)
bitwise_xor = cv.bitwise_xor(circle,rectangle)
cv.imshow('XOR',bitwise_xor)

# Bitwise NOT
# here we can see that we are getting the inverted areas 
# same can be done with rectangle 
bitwise_not = cv.bitwise_not(circle)
cv.imshow('NOT',bitwise_not)


cv.waitKey(0)