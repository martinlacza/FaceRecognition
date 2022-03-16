import face_recognition
import numpy as np
import cv2

video_capture = cv2.VideoCapture(0)

import pickle
pickle_in = open("mlp.pickle","rb")
mlp = pickle.load(pickle_in)

pickle_in = open("mlpNose.pickle","rb")
mlpNose = pickle.load(pickle_in)


video_capture = cv2.VideoCapture(0)


while True:
    ret, frame = video_capture.read()
    rgb_frame = frame[:,:,::-1]

    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame,face_locations)

    for(top,right, bottom,left), face_encodings in zip(face_locations,face_encodings):
        gender = mlp.predict(face_encodings.reshape(1,-1))
        nose = mlpNose.predict(face_encodings.reshape(1,-1))
        print(gender == '1')
        if gender == '1':
            gender = 'Male'
        if gender == '-1':
            gender = 'Female'
        if nose == '1':
            nose = 'Big Nose'
        if nose == '-1':
            nose = 'Small Nose'

        output = gender + ', ' + nose

        cv2.rectangle(frame, (left, bottom - 35), (right,bottom), (0,0,255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame,output,(left + 6, bottom - 6),font, 1.0,(255,255,255),1)

    cv2.imshow("Video", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
video_capture.release()
cv2.destroyAllWindows()