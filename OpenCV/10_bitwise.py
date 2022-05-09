import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
#255 is color white, and -1 fills entire img
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)
#200 is radius

# cv.imshow("rectangle", rectangle)
# cv.imshow("circle", circle)

#bitwise AND
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow("BW AND", bitwise_and)
#Places two images on top of one another and only displays the intersection

#bitwise OR
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow("BW OR", bitwise_or)
#Returns both bitwise_and, as well as non-intersecting regions

#bitwise XOR
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow("BW XOR", bitwise_xor)
#Returns only non-intersecting regions

#bitwise NOT
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow("BW NOT", bitwise_not)
#Inverts all values in img

cv.waitKey(0)