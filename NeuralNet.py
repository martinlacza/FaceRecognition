import pickle
pickle_in = open("trainX.pickle","rb")
X = pickle.load(pickle_in)


pickle_in = open("trainY.pickle","rb")
Y = pickle.load(pickle_in)

pickle_in = open("testX.pickle","rb")
testX = pickle.load(pickle_in)

pickle_in = open("testY.pickle","rb")
testY = pickle.load(pickle_in)

from sklearn.neural_network import MLPClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

mlp = MLPClassifier(hidden_layer_sizes=(128,),validation_fraction=0.1,early_stopping=True, max_iter=1000, alpha=1e-8,solver='sgd', verbose=10, tol=1e-4, random_state=1,learning_rate_init=.01)
s = mlp.fit(X,Y)
liss_value = mlp.loss_curve_
val = mlp.validation_scores_
pickle_out = open("mlp.pickle","wb")
pickle.dump(s,pickle_out)
pickle_out.close()
print(mlp.score(testX, testY))
import face_recognition
known_face = face_recognition.load_image_file("lada.jpg")
known_face_encoding = face_recognition.face_encodings(known_face)[0]

print(mlp.predict(known_face_encoding.reshape(1,-1)))
from matplotlib import pyplot as plt
plt.plot(liss_value)
plt.show()
plt.plot(val)
plt.show()

pickle_in = open("trainNoseX.pickle","rb")
Xnose = pickle.load(pickle_in)


pickle_in = open("trainNoseY.pickle","rb")
Ynose = pickle.load(pickle_in)

pickle_in = open("testNoseX.pickle","rb")
testXnose = pickle.load(pickle_in)

pickle_in = open("testNoseY.pickle","rb")
testYnose = pickle.load(pickle_in)

mlp = MLPClassifier(hidden_layer_sizes=(128,),validation_fraction=0.1,early_stopping=True, max_iter=1000, alpha=1e-4,solver='adam', verbose=10, tol=1e-4, random_state=1,learning_rate_init=.005)
sNose = mlp.fit(Xnose,Ynose)
liss_value = mlp.loss_curve_
val = mlp.validation_scores_
pickle_out = open("mlpNose.pickle","wb")
pickle.dump(sNose,pickle_out)
pickle_out.close()
print(mlp.score(testXnose, testYnose))
import face_recognition
known_face = face_recognition.load_image_file("lada.jpg")
known_face_encoding = face_recognition.face_encodings(known_face)[0]

print(mlp.predict(known_face_encoding.reshape(1,-1)))
from matplotlib import pyplot as plt
#plt.plot(liss_value)
#plt.show()
#plt.plot(val)
#plt.show()