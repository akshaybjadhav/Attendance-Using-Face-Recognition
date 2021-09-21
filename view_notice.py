from tkinter import *
import sqlite3
import os
import sys
from PIL import ImageTk, Image
import cv2

root = Tk()
root.geometry('830x500')
root.title("ATTENDANCE VIA FACE RECOGNITION SYSTEM")
root.configure(background="#123C69")
root.resizable(0,0)

uname=StringVar()
pwd=StringVar()

label_0 = Label(root, text="ATTENDANCE VIA FACE RECOGNITION SYSTEM",bg="#123C69",fg="#FFFFFF", width=50,font=("Algerian", 20))
label_0.place(x=-5,y=30)


def home():
   root.destroy()
   os.system('student_home.py')
   
def logout():
   root.destroy()
   os.system('home.py')

def database():
   name1=uname.get()
   conn = sqlite3.connect('Form1.db')
   with conn:
      cursor = conn.cursor()
   cursor.execute('SELECT * FROM notice')
   result_set = cursor.fetchall()
   conn.commit()
   u=23
   s=90
   i=1;
   p=35;
   for row in result_set:
      content=row[1]
      date=row[2]
      print(content)
      print(date)
      print(s+(u*i))
      if(i==1):
         label_4 = Label(root, text=date,fg="#000000",bg="#cffdbc", width=13,height=3,font=("", 9))
         label_4.place(x=0,y=s+(u*i))
         label_5 = Label(root, text=content,fg="#000000",bg="#cffdbc", width=110,height=3,font=("", 9))
         label_5.place(x=100,y=s+(u*i))

      if(i>1):
         s=s+p
         label_4 = Label(root, text=date,fg="#000000",bg="#cffdbc", width=13,height=3,font=("", 9))
         label_4.place(x=0,y=s+(u*i))
         label_5 = Label(root, text=content,fg="#000000",bg="#cffdbc", width=110,height=3,font=("", 9))
         label_5.place(x=100,y=s+(u*i))
      i=i+1;
      

#first row
Button(root, text='Home',width=15,height=1,bg='#FCCD04',fg='black',command=home).place(x=0,y=65)
label_11 = Label(root, text="COLLEGE NOTICE",bg="#FCCD04",width=74,height=1,font=("bold", 10))
label_11.place(x=118,y=65)
Button(root, text='Logout',width=15,bg='#FCCD04',height=1,fg='black',command=logout).place(x=719,y=65)

label_1 = Label(root, text="Date",fg="#FFFFFF",bg="#AC3B61", width=13,font=("", 9))
label_1.place(x=0,y=90)
label_1 = Label(root, text="Notice",fg="#FFFFFF",bg="#AC3B61", width=110,font=("", 9))
label_1.place(x=100,y=90)

database()

root.mainloop()

























