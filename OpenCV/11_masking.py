import cv2 as cv
import numpy as np

img = cv.imread("Photos/Thane.webp")

blank = np.zeros(img.shape[:2], dtype='uint8')
#In order for masking to work, balnk img has to be same size as target img

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
#img.shape are img x and y dimensions
cv.imshow("Mask", mask)
#Mask is essentially a filter slot, can also be any shape

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow("Masked Img", masked)

cv.waitKey(0)