import sqlite3
import os
import cv2
conn = sqlite3.connect('Form1.db')
with conn:
   cursor = conn.cursor()

path = 'Faces'
sampleNum=86
imagePaths = [os.path.join(path, f)for f in os.listdir(path)]
for imagePath in imagePaths:

    ID = int(os.path.split(imagePath)[-1].split('.')[1])
    if ID==7:
        sampleNum = sampleNum + 1
        os.rename(imagePath,"Faces/User.102."+str(sampleNum)+".jpg")
