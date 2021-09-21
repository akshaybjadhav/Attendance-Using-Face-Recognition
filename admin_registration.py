from tkinter import *
import sqlite3
import os

root = Tk()
ws= root.winfo_screenwidth()
hs=root.winfo_screenheight()
x=(ws/2)-250
y=(hs/2)-250
root.geometry('%dx%d+%d+%d' % (500, 500, x, y))
root.title("ATTAINDANCE VIA FACE RECOGNITION SYSTEM")
root.configure(background="#123C69")
root.resizable(0,0)



Id = StringVar()
fname=StringVar()
lname=StringVar()
email=StringVar()
var = IntVar()
contact=StringVar()
dept=StringVar()
address=StringVar()
uname=StringVar()
pwd=StringVar()
cpwd=StringVar()

conn = sqlite3.connect('Form1.db')
with conn:
   cursor = conn.cursor()


def popupmsg(msg):
   popup=Tk()
   popup.wm_title("!")
   popup.resizable(0,0)
   label=Label(popup,text=msg,width=30,font=("bold", 10))
   label.pack(side="top",fill="x",pady=10)
   B1=Button(popup,text="OK",command=popup.destroy)
   B1.pack()
   popup.mainloop()

def home():
   root.destroy()
   os.system('home.py')
   
def login():
   root.destroy()
   os.system('login.py')

def validate():
   check = 0

   if (fname.get() != ""):
      check = check + 1
   else:
      popupmsg("Enter First Name")

   if (lname.get() != ""):
      check = check + 1
   else:
      popupmsg("Enter Last Name")

   x = contact.get()
   if (len(x) == 10 and x.isnumeric() == True):
      check = check + 1
   else:
      popupmsg("Enter Valid Contact No.")

   emailid = email.get()
   if ("" in emailid and '@' in emailid and '.' in emailid):
      check = check + 1
   else:
      popupmsg("Enter Valid Email")

   if (dept.get() != ""):
      check = check + 1
   else:
      popupmsg("Enter Department")

   if (var.get() != 0):
      check = check + 1
   else:
      popupmsg("Enter Gender")

   if (address.get() != ""):
      check = check + 1
   else:
      popupmsg("Enter Address")
   if (uname.get()==""):
      popupmsg("Enter Username")
   else:
      check=check+1
   # To avoid same Username
   unm=uname.get()
   cursor.execute('Select uname from admins where uname=?', (unm,))
   result = cursor.fetchall()
   count = 0
   for row in result:
      count = count + 1
   if (count>0):
      popupmsg("Username already exist")
   else:
      check=check+1
   if (uname.get() == pwd.get()):
      popupmsg("Username and Password Can not be same")
   else:
      check=check+1
   if (pwd.get() == ""):
      popupmsg("Enter Password")
   else:
      check = check + 1

   if(pwd.get()==cpwd.get()):
      if len(pwd.get()) > 8:
         if any(char.isupper() for char in pwd.get()):
            if any(char.isdigit() for char in pwd.get()):
               if any(char.islower() for char in pwd.get()):
                   check=check+1
               else:
                  popupmsg("password must have a small letter ")
            else:
               popupmsg("password must have a digit ")
         else:
            popupmsg("password must have a capital letter")
      else:
         popupmsg("password length must > 9 ")
   else:
      popupmsg("password & confirm password not match ")

   if (check == 12):
      storedata()
         
      
      

def storedata():
   name1=fname.get()
   name2=lname.get()
   Id1=Id.get()
   email1=email.get()
   gender1=var.get()
   contact1=contact.get()
   address1=address.get()
   dept1=dept.get()
   uname1=uname.get()
   pwd1=pwd.get()
   cpwd1=cpwd.get()
   if(gender1==1):
      gender='male'
   elif(gender1==2):
      gender='female'
   cursor.execute('CREATE TABLE IF NOT EXISTS admins (Id TEXT,fname TEXT,lname TEXT,contact TEXT,email TEXT,dept TEXT,gender TEXT,address TEXT,uname TEXT,pwd TEXT)')
   cursor.execute('INSERT INTO admins (Id,fname,lname,contact,email,dept,gender,address,uname,pwd) VALUES(?,?,?,?,?,?,?,?,?,?)',(Id1,name1,name2,contact1,email1,dept1,gender,address1,uname1,pwd1))
   conn.commit()
   conn.close()
   root.destroy()
   popupmsg("Signup Succefull")
   os.system('login.py')

#first row
label_0 = Label(root, text="ATTAINDANCE SYSTEM",bg="#123C69",fg="#FFFFFF", width=30,font=("Algerian", 20))
label_0.place(x=15,y=13)
Button(root, text='Home',width=15,height=1,bg='#FCCD04',fg='black',command=home).place(x=0,y=51)
label_1 = Label(root, text="Admin SignUp Form",bg="#FCCD04",width=33,height=1,font=("bold", 10))
label_1.place(x=118,y=51)
Button(root, text='Login',width=15,bg='#FCCD04',height=1,fg='black',command=login).place(x=391,y=51)


label_1 = Label(root, text="Id",bg="#123C69",fg="#FFFFFF",width=20,font=("bold", 10))
label_1.place(x=80,y=80)

entry_1 = Entry(root,textvar=Id)
entry_1.place(x=240,y=80)

label_2 = Label(root, text="First Name",bg="#123C69",fg="#FFFFFF",width=20,font=("bold", 10))
label_2.place(x=80,y=110)

entry_2 = Entry(root,textvar=fname)
entry_2.place(x=240,y=110)


label_3 = Label(root, text="Last Name",bg="#123C69",fg="#FFFFFF",width=20,font=("bold", 10))
label_3.place(x=80,y=140)

entry_3 = Entry(root,textvar=lname)
entry_3.place(x=240,y=140)

label_4 = Label(root, text="Contact",bg="#123C69",fg="#FFFFFF",width=20,font=("bold", 10))
label_4.place(x=80,y=170)

entry_4 = Entry(root,textvar=contact)
entry_4.place(x=240,y=170)

label_5 = Label(root, text="Email",bg="#123C69",fg="#FFFFFF",width=20,font=("bold", 10))
label_5.place(x=80,y=200)

entry_5 = Entry(root,textvar=email)
entry_5.place(x=240,y=200)

label_6 = Label(root, text="Department",bg="#123C69",fg="#FFFFFF",width=20,font=("bold", 10))
label_6.place(x=80,y=230)

entry_6 = Entry(root,textvar=dept)
entry_6.place(x=240,y=230)

label_7 = Label(root, text="Gender",bg="#123C69",fg="#FFFFFF",width=20,font=("bold", 10))
label_7.place(x=80,y=260)

Radiobutton(root, text="Male",padx = 5,bg="#123C69", variable=var, value=1).place(x=235,y=260)
Radiobutton(root, text="Female",padx = 20,bg="#123C69", variable=var, value=2).place(x=290,y=260)

label_8 = Label(root, text="Address",bg="#123C69",fg="#FFFFFF",width=20,font=("bold", 10))
label_8.place(x=80,y=290)

entry_8 = Entry(root,textvar=address)
entry_8.place(x=240,y=290)

label_9 = Label(root, text="Username",bg="#123C69",fg="#FFFFFF",width=20,font=("bold", 10))
label_9.place(x=80,y=330)

entry_9 = Entry(root,textvar=uname)
entry_9.place(x=240,y=330)


label_10 = Label(root, text="Password",bg="#123C69",fg="#FFFFFF",width=20,font=("bold", 10))
label_10.place(x=80,y=370)

entry_10 = Entry(root,textvar=pwd)
entry_10.place(x=240,y=370)

label_11 = Label(root, text="Confirm Password",bg="#123C69",fg="#FFFFFF",width=20,font=("bold", 10))
label_11.place(x=80,y=400)

entry_11 = Entry(root,textvar=cpwd)
entry_11.place(x=240,y=400)

Button(root, text='Submit',width=20,bg='#FCCD04',fg='black',command=validate).place(x=170,y=430)

root.mainloop()
