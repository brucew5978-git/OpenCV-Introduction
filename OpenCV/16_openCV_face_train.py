import os
import cv2 as cv
import numpy as np

p = []
for i in os.listdir(r'C:\Users\CITADEL\Desktop\Co-op\Projects\OpenCV\Face Train'):
    p.append(i)
#Gets all people in "Face Train" folder

print(p)

people = ['Commander Shepard']
DIR = r'C:\Users\CITADEL\Desktop\Co-op\Projects\OpenCV\Face Train'
haar_cascade = cv.CascadeClassifier('haar_face.xml')

features = []
labels = []

def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        #loops through every person in "Face Train" folder

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for(x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                #roi = Region of Interest
                #Crops face from img

                features.append(faces_roi)
                #Adds face from img to features array
                labels.append(label)
                #Where label is the index of this list (Commander Shepard = 0, as first person in folder as of 2022-4-25)
                #Label/index makes navigating btw data easy


        #loops through every img in person's folder
create_train()
print('Training Complete --------------------')

# print(f'Length of features: {len(features)}')
# print(f'Length of labels: {len(labels)}')

features = np.array(features, dtype='object')
labels = np.array(labels)
#Converts arrays to numpy arrays

face_recognizer = cv.face.LBPHFaceRecognizer_create()

#Train Recognizer on features and labels list
face_recognizer.train(features, labels)

face_recognizer.save('face_trained.yml')
#Creates yml file which allows for training data to be saved and used on other devices
np.save('features.npy', features)
np.save('labels.npy', labels)
