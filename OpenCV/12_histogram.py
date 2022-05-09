#Histograms are useful in advanced vision projects where pixel analysis is needed 


import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("Photos/Thane.webp")

blank = np.zeros(img.shape[:2], dtype='uint8')

grayscale = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow("Gray", grayscale)

circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)

mask = cv.bitwise_and(grayscale, grayscale, mask=circle)

#Histogram (Grayscale)
gray_hist = cv.calcHist([grayscale], [0], mask, [256], [0, 256])
#Visualizes info about pixel distribution for an img
#[] is list that can contain multiple imgs, and 0 is the channel for the imgs
#None is where a mask can be applied, and [256] is bins - bins are integral of pixel intensity

# plt.figure()
# plt.title("Grayscale Histogram")
# plt.xlabel("Bins")
# plt.ylabel("# of pixels")
# plt.plot(gray_hist)

# plt.xlim([0, 256])
# #Defines limits for x axis
# plt.show()

#Histogram (Color)

colorMask = cv.bitwise_and(img, img, mask=circle)

plt.figure()
plt.title("Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")
colors = ('b', 'g', 'r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])


plt.figure()
plt.title("Color Histogram Masked")
plt.xlabel("Bins")
plt.ylabel("# of pixels")
colors = ('b', 'g', 'r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img], [i], circle, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])

plt.show()

cv.waitKey(0)