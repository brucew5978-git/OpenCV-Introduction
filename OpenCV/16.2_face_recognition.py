#In typical recognizers, should at least have 1000 imgs used for training

import numpy as np
import cv2 as cv

haar_cascade = cv.CascadeClassifier('haar_face.xml')

people = ['Commander Shepard']
# features = np.load('features.npy')
# labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

img = cv.imread(r'C:\Users\CITADEL\Desktop\Co-op\Projects\OpenCV\Face Validation\mass-effect-3-alternate-ending-petition.jpg')
#img = cv.imread(r'C:\Users\CITADEL\Desktop\Co-op\Projects\OpenCV\Face Train\Commander Shepard\mele-maleshep-logo-legendary-1612481641710_160w.png')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#Detect face in img
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for(x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+w]

    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label: {people[label]} with confidence of {confidence}')

    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), thickness=2)
    #Puts text onto img, (20,20) is origin and 1.0 is font size

    cv.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), thickness=2)

cv.imshow("Detected Face", img)

cv.waitKey(0)