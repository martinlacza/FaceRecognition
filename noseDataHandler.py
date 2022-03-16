import face_recognition
list = []
with open("subFaceBigNose.txt", "r") as fp:
    for lines in fp:
        list.append(lines.strip().split(","))

for i in range(len(list)):
    print(list[i])


trainX = []
trainY = []
for i in range(4725):
    filename = list[i][0]
    print(filename)
    known_face_folder = "C:/Users/Uzivatel/Downloads/aligned/img_align_celeba/" + filename
    known_face = face_recognition.load_image_file(known_face_folder)
    print(known_face.shape)
    try:
        known_face_encoding = face_recognition.face_encodings(known_face)[0]
        trainX.append(known_face_encoding)
        trainY.append(list[i][1])
    except:
        pass


testX = []
testY = []
for i in range(4725,len(list)):
    filename = list[i][0]
    known_face_folder = "C:/Users/Uzivatel/Downloads/aligned/img_align_celeba/" + filename
    known_face = face_recognition.load_image_file(known_face_folder)
    try:
        known_face_encoding = face_recognition.face_encodings(known_face)[0]
        testX.append(known_face_encoding)
        testY.append(list[i][1])
    except:
        pass



from sklearn.svm import SVC
import pickle

pickle_out = open("trainNoseX.pickle","wb")
pickle.dump(trainX, pickle_out)
pickle_out.close()


pickle_out = open("trainNoseY.pickle","wb")
pickle.dump(trainY, pickle_out)
pickle_out.close()

pickle_out = open("testNoseX.pickle","wb")
pickle.dump(testX, pickle_out)
pickle_out.close()

pickle_out = open("testNoseY.pickle","wb")
pickle.dump(testY, pickle_out)
pickle_out.close()