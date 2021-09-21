from tkinter import *
import tkinter as tk
from tkinter import ttk
import sqlite3
import os
import cv2
from tkinter import scrolledtext
from datetime import datetime, timedelta

root = Tk()
ws= root.winfo_screenwidth()
hs=root.winfo_screenheight()
x=(ws/2)-250
y=(hs/2)-250
root.geometry('%dx%d+%d+%d' % (500, 500, x, y))
root.title("ATTENDANCE VIA FACE RECOGNITION")
root.configure(background="#123C69")
root.resizable(0,0)

conn = sqlite3.connect('Form1.db')
with conn:
   cursor = conn.cursor()

def popupmsg(msg):
   popup=Tk()
   popup.wm_title("Message!")
   popup.resizable(0,0)
   label=Label(popup,text=msg,width=30,font=("bold", 10))
   label.pack(side="top",fill="x",pady=10)
   B1=Button(popup,text="OK",command=popup.destroy)
   B1.pack()
   popup.mainloop()


def home():
   root.destroy()
   os.system('admin_home1.py')
   
def logout():
   root.destroy()
   os.system('home.py')


def database():
   content1=text_area.get('1.0', tk.END)
   #print(content1)
   now = datetime.now()
   current_date = now.strftime("%d/%m/%Y")
   current_time = now.strftime("%H:%M:%S")
   cursor.execute('CREATE TABLE IF NOT EXISTS notice (id INTEGER PRIMARY KEY AUTOINCREMENT,content TEXT,date TEXT)')
   cursor.execute('INSERT INTO notice (content,date) VALUES(?,?)',(content1,current_date))
   conn.commit()
   conn.close()
   msg = " Notice sent success! "
   popupmsg(msg)

   


#first row
label_0 = Label(root, text="ATTENDANCE SYSTEM",bg="#123C69",fg="#FFFFFF", width=30,font=("Algerian", 20))
label_0.place(x=15,y=13)
Button(root, text='Home',width=15,height=1,bg='#FCCD04',fg='black',command=home).place(x=0,y=51)
label_1 = Label(root, text="Add Notice",bg="#FCCD04",width=33,height=1,font=("bold", 10))
label_1.place(x=118,y=51)
Button(root, text='Logout',width=15,bg='#FCCD04',height=1,fg='black',command=logout).place(x=391,y=51)


label_0 = Label(root, text="Add Notice Content bellow",bg="#123C69",fg="#FFFFFF",width=20,font=("bold", 12))
label_0.place(x=160,y=90)

# Creating scrolled text 
# area widget
text_area = scrolledtext.ScrolledText(root, 
                                      wrap = tk.WORD, 
                                      width = 40,
                                      height = 10, 
                                      font = ("Times New Roman",
                                              15))
  
text_area.grid(column = 0, pady = 10, padx = 6)
text_area.place(x=35,y=120)
  
# Placing cursor in the text area
text_area.focus()


Button(root, text='Send Notice',width=20,bg='#FCCD04',fg='black',command=database).place(x=180,y=360)

root.mainloop()
