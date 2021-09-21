import os
import cv2
import numpy as np
import PIL.Image
from tkinter import *
from tkinter.ttk import *

root = Tk()
root.resizable(0,0)
root.title("Please wait")
label=Label(root,text="                 Training Data",width=30,font=("bold", 10))
label.grid(column = 0, row = 2,pady=2)
progress=Progressbar(root, orient= HORIZONTAL, length=300, mode='determinate')
progress.grid(column = 0, row = 3, pady  =5)
root.resizable(0,0)


recognizer = cv2.face.LBPHFaceRecognizer_create()
if not os.path.exists('./recognizer'):
    os.makedirs('./recognizer')
path = 'Faces'

def getImagesWithID(path):
    count=0
    imagePaths = []
    for f in os.listdir(path):
        imagePaths.append(os.path.join(path, f))
        count=count+1
    i=50/count
    a=0
    faces = []
    IDs = []
    for imagePath in imagePaths:
        a=a+i
        progress["value"] =a
        progress.update()
        img=PIL.Image.open(imagePath)
        faceImg = img.convert('L')
        faceNp = np.array(faceImg, 'uint8')
        ID = int(os.path.split(imagePath)[-1].split('.')[1])
        faces.append(faceNp)
        IDs.append(ID)
        #cv2.imshow("Training Data",faceNp)
        #cv2.waitKey(10)
    return np.array(IDs), faces
Ids, faces = getImagesWithID(path)

progress["value"] =55
progress.update()
recognizer.train(faces, Ids)
progress["value"] =80
progress.update()
recognizer.save('recognizer/trainingData.yml')
progress["value"] =100
progress.update()
root.destroy()
cv2.destroyAllWindows()
os.system('admin_home1.py')

root.mainloop()
