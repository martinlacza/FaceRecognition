import os
import shutil
folder = "C:/Users/Uzivatel/Downloads/newStuff/CelebA-small"
path = "C:/Users/Uzivatel/Downloads/aligned/img_align_celeba"

list = []
with open("list_attr_celeba.txt","r") as fp:
    for lines in fp:
        list.append(lines.strip().split(" "))

for i in range(1,len(list[1])):

    print(i,list[1][i],list[2][i])

subgroupFaces = []
for filename in os.listdir(folder):
    subgroupFaces.append(filename)

subFaceGender = []
for i in range(len(subgroupFaces)):
    faceGender = []
    for j in range(2,len(list)):
        if subgroupFaces[i] == list[j][0]:
            faceGender.append(subgroupFaces[i])
            faceGender.append(list[j][21])
            subFaceGender.append(faceGender)
with open("subFaceGender.txt","w") as fp:
    for i in range(len(subFaceGender)):
        print(subFaceGender[i],file=fp)

print(len(subgroupFaces))
print(list[278][21])

#for filename in os.listdir(path):
    #for i in range(len(subgroupFaces)):
      #  if filename == subFaceGender[i][0]:
         #   print("FILENAME AND SUBGROUPFACE ARE", filename,subFaceGender[i][0])
        #    if int(subFaceGender[i][1]) == 1:
         #       print("copying to male",filename)
        #        shutil.copy2("C:/Users/Uzivatel/Downloads/aligned/img_align_celeba/" + filename, "C:/Users/Uzivatel/Documents/faceGender/Male/" + filename)
        #    if int(subFaceGender[i][1]) == -1:
        #        print("copying to female", filename)
         #       shutil.copy2("C:/Users/Uzivatel/Downloads/aligned/img_align_celeba/" + filename,
          #                   "C:/Users/Uzivatel/Documents/faceGender/Female/" + filename)
