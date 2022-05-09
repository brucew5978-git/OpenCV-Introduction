import cv2 as cv
import numpy as np

img = cv.imread('Photos/Thane.webp')
cv.imshow("Thane", img)

blank = np.zeros(img.shape[:2], dtype='uint8')
#Creates clank img

blue,green,red = cv.split(img)
#cv.imshow('blue', blue)
# cv.imshow('green', green)
cv.imshow('red', red)
#imgs shows white where color is intense, and black where colors are less intense

print(img.shape)
print(blue.shape)
print(green.shape)
#prints in form (550, 650, 3), where pixels are displayed, and "3" is the shape - number of colors

#Img merging
merged = cv.merge([blue,green,red])
# cv.imshow('merge', merged)
#merges colors together

blueScale = cv.merge([blue, blank, blank])
greenScale = cv.merge([blank, green, blank])
#Displays visulized color channels

cv.imshow("blue scale", blueScale)
cv.imshow("green scale", greenScale)

cv.waitKey(0)