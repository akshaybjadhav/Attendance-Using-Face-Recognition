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
   name2=pwd.get()
   name3='x';
   name4='x';
   name5='x';
   name6='x';
   name7='x';
   check=0
   conn = sqlite3.connect('Form1.db')
   with conn:
      cursor = conn.cursor()
   cursor.execute('SELECT * FROM attendance_sheet')
   result_set = cursor.fetchall()
   conn.commit()
   u=23
   s=90
   i=1;
   for row in result_set:
      name3=row[0]
      name4=row[1]
      name5=row[2]
      name6=row[3]
      name7=row[4]
      name8=row[5]
      name9=row[6]
      name10=row[7]
#      name11=row[8]
 #     name12=row[9]
      label_4 = Label(root, text=name3,fg="#000000",bg="#FCCD04", width=13,font=("", 9))
      label_4.place(x=0,y=s+(u*i))
      label_5 = Label(root, text=name4,fg="#000000",bg="#FCCD04", width=13,font=("", 9))
      label_5.place(x=100,y=s+(u*i))
      label_6 = Label(root, text=name5,fg="#000000",bg="#FCCD04", width=13,font=("", 9))
      label_6.place(x=200,y=s+(u*i))
      label_7 = Label(root, text=name6,fg="#000000",bg="#FCCD04", width=13,font=("", 9))
      label_7.place(x=300,y=s+(u*i))
      label_8 = Label(root, text=name7,fg="#000000",bg="#FCCD04", width=15,font=("", 9))
      label_8.place(x=400,y=s+(u*i))
      label_9 = Label(root, text=name8,fg="#000000",bg="#FCCD04", width=16,font=("", 9))
      label_9.place(x=514,y=s+(u*i))
      label_10 = Label(root, text=name9,fg="#000000",bg="#FCCD04", width=13,font=("", 9))
      label_10.place(x=635,y=s+(u*i))
      label_11 = Label(root, text=name10,fg="#000000",bg="#FCCD04", width=13,font=("", 9))
      label_11.place(x=735,y=s+(u*i))
    #  label_12 = Label(root, text=name11,fg="#000000",bg="#FCCD04", width=13,font=("", 9))
     # label_12.place(x=940,y=s+(u*i))
      #label_13 = Label(root, text=name12,fg="#000000",bg="#FCCD04", width=13,font=("", 10))
      #label_13.place(x=1041,y=s+(u*i))
      i=i+1;
  
   

#first row
Button(root, text='Home',width=15,height=1,bg='#FCCD04',fg='black',command=home).place(x=0,y=65)
label_11 = Label(root, text="Attendance Sheet",bg="#FCCD04",width=74,height=1,font=("bold", 10))
label_11.place(x=118,y=65)
Button(root, text='Logout',width=15,bg='#FCCD04',height=1,fg='black',command=logout).place(x=719,y=65)

label_1 = Label(root, text="Roll No",fg="#FFFFFF",bg="#AC3B61", width=13,font=("", 9))
label_1.place(x=0,y=90)
label_2 = Label(root, text='First name',fg="#FFFFFF",bg="#AC3B61", width=13,font=("", 9))
label_2.place(x=100,y=90)
label_3 = Label(root, text='Middle name',fg="#FFFFFF",bg="#AC3B61", width=13,font=("", 9))
label_3.place(x=200,y=90)
label_4 = Label(root, text='Last name',fg="#FFFFFF",bg="#AC3B61", width=13,font=("", 9))
label_4.place(x=300,y=90)
label_5 = Label(root, text='Department',fg="#FFFFFF",bg="#AC3B61", width=15,font=("", 9))
label_5.place(x=400,y=90)
label_6 = Label(root, text='Date',fg="#FFFFFF",bg="#AC3B61", width=16,font=("", 9))
label_6.place(x=514,y=90)
label_7 = Label(root, text="InTime",fg="#FFFFFF",bg="#AC3B61", width=13,font=("", 9))
label_7.place(x=635,y=90)
label_8 = Label(root, text="OutTime",fg="#FFFFFF",bg="#AC3B61", width=13,font=("", 9))
label_8.place(x=735,y=90)

database()




root.mainloop()

























