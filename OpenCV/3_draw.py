import cv2 as cv
import numpy as np

# blank = np.zeros((500, 500, 3), dtype='uint8')
# cv.imshow('Blank', blank)
#Generated blank img, where 500,500 is size, and 3 is colour counters

blume = cv.imread('Photos/Blume Logo.jpg')
# cv.imshow('Blume', blume)

# blank[:] = 0, 255,0
# cv.imshow('Green', blank)
# #Filters entire img as green

# blank[200:300 , 300:400] = 255,0,0
# cv.imshow('Green 2', blank)
#Creates block of blue in specified range

# cv.rectangle(blume, (0,0), (250,200), (0,255,0), thickness=2)
cv.rectangle(blume, (0,0), (blume.shape[1]//2, blume.shape[0]//2), (0,255,0), thickness=2)
cv.imshow('Blume M', blume)
# thickness=cv.FILLED or thickness=-1will fill rectangle

# cv.circle(blume,  (blume.shape[1]//2, blume.shape[0]//2), 40, (0,0,255), thickness=3)
# cv.imshow('Blume M2', blume)

# cv.line(blume, (0,0), (blume.shape[1]//2, blume.shape[0]//2), (0,255,0), thickness=1)
# cv.imshow('Blume M3', blume)

cv.putText(blume, 'Test', (255, 255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,0,255), thickness=2)
cv.imshow('Blume M4', blume)

cv.waitKey(0)