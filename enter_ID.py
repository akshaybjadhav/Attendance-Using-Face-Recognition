from tkinter import *
import sqlite3
import os

root = Tk()
ws= root.winfo_screenwidth()
hs=root.winfo_screenheight()
x=(ws/2)-150
y=(hs/2)-75
root.geometry('%dx%d+%d+%d' % (300, 150, x, y))
root.title("ATTENDANCE VIA FACE RECOGNITION")
root.configure(background="#123C69")
root.resizable(0,0)
rn=StringVar()

def home():
   root.destroy()
   os.system('admin_home1.py')

def popupmsg(msg):
   popup=Tk()
   popup.wm_title("!")
   popup.resizable(0,0)
   label=Label(popup,text=msg,width=30,font=("bold", 10))
   label.pack(side="top",fill="x",pady=10)
   B1=Button(popup,text="OK",command=popup.destroy)
   B1.pack()
   popup.mainloop()


def database():
   rnm=rn.get()
   check=0
   conn = sqlite3.connect('Form1.db')
   with conn:
      cursor = conn.cursor()
   cursor.execute('SELECT fname FROM student WHERE id=? ',(rnm,))
   result_set = cursor.fetchall()
   conn.commit()
   for row in result_set:
      check=check+1
   
   if(check==0):
      popupmsg("ID not Available")
   if(check==1):
      myfun()


def myfun():
   rn1=rn.get()
   new="python update.py --id "+str(rn1)
   print(rn1+"yeeeeeeeeeeee")
   root.destroy()
   os.system(new)


label_1edt = Label(root, text="Enter ID",bg="#123C69",fg="#FFFFFF",width=20,font=("bold", 10))
label_1edt.place(x=1,y=40)
entry_1edt = Entry(root,textvar=rn)
entry_1edt.place(x=150,y=40)
Button(root, text='Home',width=20,bg='#FCCD04',fg='black',command=home).place(x=1,y=75)
Button(root, text='Next',width=20,bg='#FCCD04',fg='black',command=database).place(x=150,y=75)
root.mainloop()







