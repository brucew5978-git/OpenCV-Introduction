#From a programing perspective, gradians are similar to edges (Very different mathematically)

import cv2 as cv
import numpy as np

img = cv.imread('Photos/Thane.webp')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
#Where cv.CV_64F = ddepth
lap = np.uint8(np.absolute(lap))
#When pixel goes from black to white, considered mathematically as +ve or -ve slope. However, as pixels cannot have -ve value, so the absolute value is taken
#This value is then converted into uint8 = img specific datatype
cv.imshow("Laplacion", lap)
# *Visiually similar to Watch_Dogs graphics

#Sobel 
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
#1 = x direction, 0 = y direction
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combine_sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow("Sobel X", sobelx)
cv.imshow("Combined Sobel", combine_sobel)

canny = cv.Canny(gray, 150, 175)
cv.imshow("Canny", canny)
#Canny is a more advanced edge detection algorithm that involves sobel in one of its process

cv.waitKey(0)