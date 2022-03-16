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

subFaceBigNose = []
for i in range(len(subgroupFaces)):
    faceBigNose = []
    for j in range(2,len(list)):
        if subgroupFaces[i] == list[j][0]:
            faceBigNose.append(subgroupFaces[i])
            faceBigNose.append(list[j][8])
            subFaceBigNose.append(faceBigNose)
with open("subFaceBigNose.txt","w") as fp:
    for i in range(len(subFaceBigNose)):
        print(subFaceBigNose[i],file=fp)

print(len(subgroupFaces))
print(list[278][21])