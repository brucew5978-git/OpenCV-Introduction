import cv2 as cv

img = cv.imread('Photos/Thane.webp')
cv.imshow("Thane", img)

#Averaging
average = cv.blur(img, (3,3))
#cv.imshow("Average", average)
#Where (7,7) is kernal size for reducing resolution. Blurring kernal needs to be odd, as center pixel is output in new img

#Gaussian
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow("Gauss", gauss)
#0 is the standard deviation

#Similar to Averaging, but each pixel is given a specific weight instead of a standard average 
#Will tend to get less blur than Averaging but blurring is more natural


#Median
median = cv.medianBlur(img, 3)
cv.imshow("Median", median)
#3 is the kernal size - openCV assumes kernal size from int
#Reduces more noise than Averaging or Gaussian. Most effective at low kernal sizes

#Bilateral
bilateral = cv.bilateralFilter(img, 10, 35, 35)
cv.imshow("Bilateral", bilateral)
#35 values are sigma values - describes how far away pixels will influence the blurred pixel
#Most effective blurring method, applies blurring but retains edges in img

cv.waitKey(0)