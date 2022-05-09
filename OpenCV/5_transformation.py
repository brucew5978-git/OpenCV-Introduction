import cv2 as cv
import numpy as np

img = cv.imread('Photos/ctOS C.jpg')
#cv.imshow('ctOS', img)

#Translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    #Gets img width and height
    return cv.warpAffine(img, transMat, dimensions)

#-x = shift to left
#-y = shoft up

translated = translate(img, 100, 100)
cv.imshow('translated', translated)


#Rotations
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    
    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    #1.0 is scale of image

    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 45)
#-45 is rotation in other direction
#Can also rotate a rotated img
#cv.imshow('rotated', rotated)

#Resizing
resized = cv.resize(img, (1500, 1500), interpolation=cv.INTER_CUBIC)
#cv.imshow('resized', resized)

#Flip
flip = cv.flip(img, 1)
#0 is flipping on x axis, 1 is flipping on y axis, and -1 is both
#cv.imshow('flip', flip)

#Cropping
cropped = img[200:400, 300:400]
cv.imshow('cropped', cropped)

cv.waitKey(0)