import cv2 as cv

img = cv.imread("Photos/Thane.webp")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#Simple Thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
#Where 150=threshold value, 255=value that pixel should be set to if greater than threshold value
#threshold returns 150 or threshold value while thresh returns grayscale img
cv.imshow("Simple Threshold", thresh)

threshold, thresh_inv = cv.threshold(gray, 100, 255, cv.THRESH_BINARY_INV)
#Gets inverse of thresh
cv.imshow("Simple Threshold Inverse", thresh_inv)

#Downside to simple threshold is that have to manually specify threshold value

#Adapted Thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
#cv.ADAPTIVE_THRESH_MEAN_C takes the mean of the pixels, 11 is the block size, and 3 is the c value (default value subtracted from the mean)
cv.imshow("Adaptive Thresh", adaptive_thresh)

adaptive_thresh_g = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow("Adaptive Thresh G", adaptive_thresh_g)

cv.waitKey(0)