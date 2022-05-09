#Pretrained OpenCV classifiers for edge detection includes Haar Cascades and Local Binary Patterns (more advanced pattern)
#Haar Cascades are popular, but not the most advanced in face detection, but easy to use
import cv2 as cv

def rescaleFrame(frame, scale = 0.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)
    
img = cv.imread('Photos/Thane.webp')
resize = rescaleFrame(img)
cv.imshow('Person', resize)

gray = cv.cvtColor(resize, cv.COLOR_BGR2GRAY)
#Face detection does not need img to be in color

haar_cascade = cv.CascadeClassifier('haar_face.xml')
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6)
#minNeighbors specifies how many rectangles/neighbors should be called a face. Higher minNeighbors value will reduce noise detected, while lower value gives more liberal face detection
#faces_rect returns rectangle coordinates for face detected

print(f'Faces Found: {len(faces_rect)}')

for(x,y,w,h) in faces_rect:
    cv.rectangle(resize, (x,y), (x+w, y+h), (0, 255, 0), thickness=2)

cv.imshow("Detected Faces", resize)
#Haar Cascades are very sensitive to noise in an img, can often detect faces in non-face objects
#Can also use haar cascades on video by scanning each frame (see 2_rescale.py for forloop template)
cv.waitKey(0)
