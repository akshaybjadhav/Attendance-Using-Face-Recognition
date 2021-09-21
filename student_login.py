from tkinter import *
import sqlite3
import os
from PIL import ImageTk, Image

root = Tk()
ws= root.winfo_screenwidth()
hs=root.winfo_screenheight()
x=(ws/2)-250
y=(hs/2)-250
root.geometry('%dx%d+%d+%d' % (500, 500, x, y))
root.title("ATTENDANCE VIA FACE RECOGNITION SYSTEM")
root.configure(background="#123C69")
root.resizable(0,0)

uname=StringVar()
pwd=StringVar()



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
   name1=uname.get()
   name2=pwd.get()
   check=0
   conn = sqlite3.connect('Form1.db')
   with conn:
      cursor = conn.cursor()
   cursor.execute('SELECT uname FROM students WHERE uname=?  AND pwd=?',(name1,name2))
   result_set = cursor.fetchall()
   conn.commit()
   for row in result_set:
      check=check+1
   

   if(check==0):
      print("............Login Not successfull")
      popupmsg("Enter valid Credentials")
   if(check==1):
      print("****************Login  successfull")
      root.destroy()
      os.system('student_home.py')


def forgotpwd():
   root.destroy()
   os.system('forgot_pwd_student.py')

def home():
   root.destroy()
   os.system('home.py')
   
def signup():
   root.destroy()
   os.system('student_registration.py')



#first row
label_0 = Label(root, text="ATTENDANCE SYSTEM",bg="#123C69",fg="#FFFFFF", width=30,font=("Algerian", 20))
label_0.place(x=15,y=13)
Button(root, text='Home',width=15,height=1,bg='#FCCD04',fg='black',command=home).place(x=0,y=67)
label_1 = Label(root, text="Student Login Form",bg="#FCCD04",width=33,height=1,font=("bold", 10))
label_1.place(x=118,y=67)
Button(root, text='Signup',width=15,bg='#FCCD04',height=1,fg='black',command=signup).place(x=391,y=67)
  
   
   
             
#label_0 = Label(root, text="Login Form",bg="#123C69",fg="#FFFFFF", width=20,font=("bold", 12))
#label_0.place(x=130,y=381)


label_1 = Label(root, text="UserName",bg="#123C69",fg="#FFFFFF",width=20,font=("bold", 10))
label_1.place(x=100,y=410)

entry_1 = Entry(root,textvar=uname)
entry_1.place(x=240,y=410)


label_2 = Label(root, text="Password",bg="#123C69",fg="#FFFFFF",width=20,font=("bold", 10))
label_2.place(x=100,y=440)

entry_2 = Entry(root,textvar=pwd)
entry_2.place(x=240,y=440)
#label_4 = Label(root, text="Programming",width=20,font=("bold", 10))
#label_4.place(x=85,y=330)
#var2= IntVar()
#Checkbutton(root, text="java", variable=var1).place(x=235,y=330)
#Checkbutton(root, text="python", variable=var2).place(x=290,y=330)
#Button(root, text='Submit',width=20,bg='brown',fg='white',command=database).place(x=180,y=470)
Button(root, text='Forgot',width=20,bg='#FCCD04',fg='black',command=forgotpwd).place(x=120,y=470)
Button(root, text='Login',width=20,bg='#FCCD04',fg='black',command=database).place(x=270,y=470)

path = "i1.jpg"

#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(Image.open(path))

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = Label(root, image = img,bg="#123C69")
panel.config( width=500 )
panel.config( height=310 )
panel.config( anchor="center" )
#panel.place(x=8,y=10)
#panel.place(x=150,y=160)

#The Pack geometry manager packs widgets in rows or columns.
panel.pack(side = "left",anchor="center")#side = "up", fill = "both", expand = "yes")

root.mainloop()

























