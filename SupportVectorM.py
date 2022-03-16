from sklearn.svm import SVC

import pickle
pickle_in = open("trainX.pickle","rb")
X = pickle.load(pickle_in)


pickle_in = open("trainY.pickle","rb")
Y = pickle.load(pickle_in)

pickle_in = open("testX.pickle","rb")
testX = pickle.load(pickle_in)

pickle_in = open("testY.pickle","rb")
testY = pickle.load(pickle_in)

model = SVC(gamma='auto')
model.fit(X,Y)
print(model.score(testX,testY))


import face_recognition
known_face = face_recognition.load_image_file("woma.jpg")
known_face_encoding = face_recognition.face_encodings(known_face)[0]
print(model.predict(known_face_encoding.reshape(1,-1)))

pickle_in = open("trainNoseX.pickle","rb")
Xnose = pickle.load(pickle_in)


pickle_in = open("trainNoseY.pickle","rb")
Ynose = pickle.load(pickle_in)

pickle_in = open("testNoseX.pickle","rb")
testXnose = pickle.load(pickle_in)

pickle_in = open("testNoseY.pickle","rb")
testYnose = pickle.load(pickle_in)
model2 = SVC(gamma='auto')
model2.fit(Xnose,Ynose)
from matplotlib import pyplot as plt
print(model2.score(testXnose,testYnose))