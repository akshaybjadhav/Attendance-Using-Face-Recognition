from tkinter import *
import sqlite3
import os

root = Tk()
ws= root.winfo_screenwidth()
hs=root.winfo_screenheight()
x=(ws/2)-150
y=(hs/2)-75
root.geometry('%dx%d+%d+%d' % (300, 150, x, y))
root.title("ATTENDANCE VIA FACE RECOGNITION SYSTEM")
root.configure(background="#123C69")
root.resizable(0,0)
id=StringVar()

conn = sqlite3.connect('Form1.db')
with conn:
   cursor = conn.cursor()


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


def validate():
   ids = id.get()
   check = 0
   cursor.execute('SELECT fname FROM student WHERE id=? ', (ids,))
   result_set = cursor.fetchall()
   conn.commit()
   for row in result_set:
      check = check + 1

   if (check == 0):
      popupmsg("ID does not exist")
   if (check == 1):
      database()


def database():
   ids=id.get()
   i = 100
   while (i != 0):
         os.remove('Faces/User.' + str(ids) + '.' + str(i) + '.jpg')
         i = i - 1
   cursor.execute('DELETE FROM student WHERE id=? ', (ids,))
   conn.commit()
   conn.close()
   root.destroy()
   popupmsg("Record deleted successfuly for ID:"+str(ids)+"\nClick OK to train data")
   os.system('trainer.py')



label_1edt = Label(root, text="Enter ID",bg="#123C69",fg="#FFFFFF",width=20,font=("bold", 10))
label_1edt.place(x=1,y=40)
entry_1edt = Entry(root,textvar=id)
entry_1edt.place(x=150,y=40)
Button(root, text='Home',width=20,bg='#FCCD04',fg='black',command=home).place(x=1,y=75)
Button(root, text='Delete Record',width=20,bg='#FCCD04',fg='black',command=validate).place(x=150,y=75)
root.mainloop()







