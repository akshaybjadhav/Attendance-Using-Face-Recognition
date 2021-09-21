from tkinter import *
import sqlite3
import os

root = Tk()
ws= root.winfo_screenwidth()
hs=root.winfo_screenheight()
x=(ws/2)-250
y=(hs/2)-150
root.geometry('%dx%d+%d+%d' % (500, 300, x, y))
root.title("ATTAINDANCE VIA FACE RECOGNITION SYSTEM")
root.configure(background="#123C69")
root.resizable(0,0)

Id = StringVar()
fname=StringVar()
lname=StringVar()
dept=StringVar()
pwd="xx"


def home():
   root.destroy()
   os.system('home.py')
   
def login():
   root.destroy()
   os.system('login.py')

def popupmsg(msg):
   popup=Tk()
   popup.wm_title("!")
   popup.resizable(0,0)
   label=Label(popup,text=msg,width=30,font=("bold", 10))
   label.pack(side="top",fill="x",pady=10)
   B1=Button(popup,text="OK",command=popup.destroy)
   B1.pack()
   popup.mainloop()
   



#def validate():
#   if(len(contact.get())==10 )



      
      

def storedata():
   Id1=Id.get()
   name1=fname.get()
   name2=lname.get()
   #dept1=dept.get()
   check=0
   conn = sqlite3.connect('Form1.db')
   with conn:
      cursor = conn.cursor()
   cursor.execute('SELECT pwd FROM students WHERE Id=? AND fname=? AND lname=?',(Id1,name1,name2))
   result_set = cursor.fetchall()
   conn.commit()
   for row in result_set:
      check=check+1
      pwd=row[0]
      
   

   if(check==0):
      print("............Login Not successfull")
      popupmsg("Enter valid Credentials")
   if(check==1):
      print("****************Login  successfull")
      root.destroy()
      popupmsg("Your Password is :"+pwd)
      os.system('student_login.py')
   


#first row
label_01 = Label(root, text="ATTAINDANCE SYSTEM",bg="#123C69",fg="#FFFFFF", width=30,font=("Algerian", 20))
label_01.place(x=15,y=13)
Button(root, text='Home',width=15,height=1,bg='#FCCD04',fg='black',command=home).place(x=0,y=51)
label_11 = Label(root, text="Forget Password Form",bg="#FCCD04",width=33,height=1,font=("bold", 10))
label_11.place(x=118,y=51)
Button(root, text='Login',width=15,bg='#FCCD04',height=1,fg='black',command=login).place(x=391,y=51)


label_1 = Label(root, text="Id",bg="#123C69",fg="#FFFFFF",width=20,font=("bold", 10))
label_1.place(x=80,y=90)

entry_1 = Entry(root,textvar=Id)
entry_1.place(x=240,y=90)

label_2 = Label(root, text="First Name",bg="#123C69",fg="#FFFFFF",width=20,font=("bold", 10))
label_2.place(x=80,y=120)

entry_2 = Entry(root,textvar=fname)
entry_2.place(x=240,y=120)


label_3 = Label(root, text="Last Name",bg="#123C69",fg="#FFFFFF",width=20,font=("bold", 10))
label_3.place(x=80,y=150)

entry_3 = Entry(root,textvar=lname)
entry_3.place(x=240,y=150)

#label_4 = Label(root, text="Year",bg="#123C69",fg="#FFFFFF",width=20,font=("bold", 10))
#label_4.place(x=80,y=180)

#entry_4 = Entry(root,textvar=dept)
#entry_4.place(x=240,y=180)

Button(root, text='Submit',width=20,bg='#FCCD04',fg='black',command=storedata).place(x=170,y=180)

root.mainloop()























