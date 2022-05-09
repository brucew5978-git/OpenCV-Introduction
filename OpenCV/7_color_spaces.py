import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Photos/Thane.webp')
#cv.imshow('img', img)

# plt.imshow(img)
# plt.show()
#Uses matplot to display img
#matplotlib displays imgs in inverse colour unlike cv

#BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray', gray)

#BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
#cv.imshow("HSV", hsv)
#HSV displays img in terms of saturation and value

#BGR to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
#cv.imshow("LAB", lab)

#BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
#cv.imshow("RGB", rgb)

# plt.imshow(rgb)
# plt.show()
#Matplotlib takes rgb img so this displays close to the original img

#HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow("HSV -> BGR", hsv_bgr)
#Any type of img can be converted to any other type using openCV - exception with converting from grayscale

cv.waitKey(0)