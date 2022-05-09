import cv2 as cv
import numpy as np

img = cv.imread('Photos/Thane.webp')

cv.imshow('Thane', img)

blank = np.zeros(img.shape, dtype='uint8')
#Blank img, can be used to draw contours onto blank to have visual demonstration of contours found by openCV
# cv.imshow('blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('gray', gray)

# blur = cv.GaussianBlur(gray, (3,3), cv.BORDER_DEFAULT)
# cv.imshow("Blur", blur)

# canny = cv.Canny(blur, 125, 175)
# cv.imshow("Canny Edge", canny)

#2nd way of finding contours
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
#Binarizes img, depending on pixel intensity below or above 125
#Turns img to black or white pixels
#cv.imshow('Thresh', thresh)

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
#Looks at a canny img and returns contours - outline/line relationships, and hierarchies
#RETR_LIST returns all contours, RETR_EXTERNAL returns external contours, RETR_TREE returns contours in hierarchy system
#CHAIN_APPROX_NONE returns all contours, CHAIN_APPROX_SIMPLE returns simplified points - compressed points

print(f'{len(contours)} contours found')

contours, hierarchies = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contours found')
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found')

cv.drawContours(blank, contours, -1, (0,255,0), 1)
#-1 specifies contour index - or how many contours will be displayed in the img, -1 means display all
#(0,0,255), 2, is colour and thickness of lines
cv.imshow('Contours Drawn', blank)

#Canny vs contours
#Canny and Contours are not the same thing, as cannies are edges, while contours are outlines, but they are similar
#Recommends feeding canny into contours instead of using threshold, as threshold has its limits
cv.waitKey(0)