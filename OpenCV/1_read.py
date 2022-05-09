import cv2 as cv

# img = cv.imread('Photos/Blume Logo.jpg')
# #Note that openCV cannot read images that are too large - like Blume Logo_large.jpg

# cv.imshow('Blume', img)
# #where "Blume" is the name of the window displaying the img

# cv.waitKey(0)
#Waits for a delay for key to be pressed, in this case, it waits forever 

#capture = cv.VideoCapture(0)
#Where the number in videoCapture is related to the web cam that is connected

capture = cv.VideoCapture('Videos/LIM Levitation.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow("Video", frame)
    #CV will display videos frame by frame

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()

