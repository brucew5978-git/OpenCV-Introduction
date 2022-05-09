import cv2 as cv

ctOS = cv.imread('Photos/ctOS C.jpg')
cv.imshow('ctOS', ctOS)

# gray = cv.cvtColor(ctOS, cv.COLOR_BGR2GRAY)
# cv.imshow('ctOS Gray', gray)
#Gray scales image

#Gaussian Blur
blur = cv.GaussianBlur(ctOS, (7,7), cv.BORDER_DEFAULT)
# cv.imshow('ctOS Blur', blur)
#(3,3) is kernal size used to converge group of pixel, into single pixel which effectively blurs image

#Canny Edge Cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow('ctOS EC', canny)
#Can pass in the blurred img for better edge detection - reduces number of edges

#Dilate img
dilated = cv.dilate(canny, (7,7), iterations=3)
#cv.imshow('Dilated', dilated)
#Expands connected sets of 1s in binary img, cna be used to grow features, or to fill holes

#Eroding
eroded = cv.erode(dilated, (7,7), iterations=3)
#cv.imshow('Erode', eroded)
#Can reverse the effects of dilation, should be very similar to cascade

#Resize
resize = cv.resize(ctOS, (500, 500), interpolation=cv.INTER_CUBIC)
#cv.imshow('Resized', resize)
#Resizing without interpolation ignores aspect ratio

#Cropping
cropped = ctOS[50:200, 200:400]
cv.imshow("Cropped", cropped)

cv.waitKey(0)
