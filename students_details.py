from tkinter import *
import sqlite3
import os
import cv2

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

id=StringVar()
fname=StringVar()
mname=StringVar()
lname=StringVar()
email=StringVar()
address=StringVar()
var = IntVar()
seq = IntVar()
contact=StringVar()
email=StringVar()
dept=StringVar()
dob=StringVar()
address=StringVar()
c=StringVar()

def popupmsg(msg):
   popup=Tk()
   popup.wm_title("Message!")
   popup.resizable(0,0)
   label=Label(popup,text=msg,width=30,font=("bold", 10))
   label.pack(side="top",fill="x",pady=10)
   B1=Button(popup,text="OK",command=popup.destroy)
   B1.pack()
   popup.mainloop()
def popupmsg2(msg):
   popup=Tk()
   popup.wm_title("Message!")
   popup.resizable(0,0)
   label=Label(popup,text=msg,width=30,font=("bold", 10))
   label.pack(side="top",fill="x",pady=10)
   B1=Button(popup,text="Ok and record face",command=lambda:[root.destroy(), popup.destroy(),record()])
   B1.pack()
   popup.mainloop()

def home():
   root.destroy()
   os.system('admin_home1.py')
   
def logout():
   root.destroy()
   os.system('home.py')

def validate():
   check=0
   if (fname.get() != ""):
      check = check + 1
   else:
      popupmsg("Enter First Name")

   if (mname.get() != ""):
      check = check + 1
   else:
      popupmsg("Enter Middle Name")

   if (lname.get() != ""):
      check = check + 1
   else:
      popupmsg("Enter Last Name")

   x = contact.get()
   if (len(x) == 10 and x.isnumeric() == True):
      check = check + 1;
   else:
      popupmsg("Contact No. Invalid")

   emailid = email.get()
   if ("" in emailid and '@' in emailid and '.' in emailid):
            check = check + 1
   else:
      popupmsg("Enter Valid Email")

   if (dept.get() != "Select Department"):
      check = check + 1
   else:
      popupmsg("Select Department")

   if (var.get() != 0):
      check = check + 1
   else:
      popupmsg("Enter Gender")

   if (address.get() != ""):
      check = check + 1
   else:
      popupmsg("Enter Address")

   if (dob.get() != ""):
      check = check + 1
   else:
      popupmsg("Enter DOB")
   if(check==9):
      database()

def database():

   name1=fname.get()
   name2=mname.get()
   name3=lname.get()
   gender1=var.get()
   dept1=dept.get()
   email1=email.get()
   contact1=contact.get()
   dob1=dob.get()
   address1=address.get()
   if(gender1==1):
      gender='male'
   elif(gender1==2):
      gender='female'

   cursor.execute('Select MAX(id) from student where dept =?', (dept1,))
   rslt = cursor.fetchone()
   id = rslt[0]
   global newid
   if id== None:
      if dept1=='First': branch=100
      if dept1 == 'Second': branch = 200
      if dept1 == 'Third': branch = 300
      if dept1 == 'Fourth': branch = 400
      newid= branch +1
   else:
      newid = id + 1

   cursor.execute('CREATE TABLE IF NOT EXISTS student (roll TEXT,fname TEXT,mname TEXT,lname TEXT,contact TEXT,email TEXT,gender TEXT,address TEXT,dept TEXT,dob TEXT)')
   cursor.execute('INSERT INTO student (id,fname,mname,lname,contact,email,gender,address,dept,dob) VALUES(?,?,?,?,?,?,?,?,?,?)',(newid,name1,name2,name3,contact1,email1,gender,address1,dept1,dob1))
   conn.commit()
   conn.close()
   msg = " Plese note your ID: " + str(newid)
   popupmsg2(msg)

def record():
   if not os.path.exists('./Faces'):
      os.makedirs('./Faces')
   face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
   cap = cv2.VideoCapture(0)        #for capturing contents from live video
   #cap=cv2.VideoCapture('vdi.mp4')   #for capturing contents from recorded video

   uid = newid
   sampleNum = 0
   while True:
      ret,img = cap.read()
      cv2.putText(img, str("Please Look into the camera till 100"), (20, 30),cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
      gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
      faces = face_cascade.detectMultiScale(gray, 1.3, 5)
      for (x,y,w,h) in faces:
         sampleNum = sampleNum+1
         cv2.imwrite("Faces/User."+str(uid)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
         cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
         cv2.putText(img,str(sampleNum), (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
         cv2.waitKey(100)
      cv2.imshow('img',img)
      cv2.waitKey(1);
      if sampleNum > 99:
         break
   cap.release()
   cv2.destroyAllWindows()
   os.system('trainer.py')
   


#first row
label_0 = Label(root, text="ATTENDANCE SYSTEM",bg="#123C69",fg="#FFFFFF", width=30,font=("Algerian", 20))
label_0.place(x=15,y=13)
Button(root, text='Home',width=15,height=1,bg='#FCCD04',fg='black',command=home).place(x=0,y=51)
label_1 = Label(root, text="Add New Student Record Form",bg="#FCCD04",width=33,height=1,font=("bold", 10))
label_1.place(x=118,y=51)
Button(root, text='Logout',width=15,bg='#FCCD04',height=1,fg='black',command=logout).place(x=391,y=51)


label_0 = Label(root, text="All fileds are Mandatory",bg="#123C69",fg="#FFFFFF",width=20,font=("bold", 10))
label_0.place(x=160,y=90)

label_1 = Label(root, text="First Name",bg="#123C69",fg="#FFFFFF",width=20,font=("bold", 10))
label_1.place(x=80,y=120)

entry_1 = Entry(root,textvar=fname)
entry_1.place(x=240,y=120)

label_1 = Label(root, text="Middle Name",bg="#123C69",fg="#FFFFFF",width=20,font=("bold", 10))
label_1.place(x=80,y=150)

entry_1 = Entry(root,textvar=mname)
entry_1.place(x=240,y=150)


label_1 = Label(root, text="Last Name",bg="#123C69",fg="#FFFFFF",width=20,font=("bold", 10))
label_1.place(x=80,y=180)

entry_1 = Entry(root,textvar=lname)
entry_1.place(x=240,y=180)

label_1 = Label(root, text="contact",bg="#123C69",fg="#FFFFFF",width=20,font=("bold", 10))
label_1.place(x=80,y=210)

entry_1 = Entry(root,textvar=contact)
entry_1.place(x=240,y=210)

label_1 = Label(root, text="Email",bg="#123C69",fg="#FFFFFF",width=20,font=("bold", 10))
label_1.place(x=80,y=240)

entry_1 = Entry(root,textvar=email)
entry_1.place(x=240,y=240)

label_1 = Label(root, text="Year",bg="#123C69",fg="#FFFFFF",width=20,font=("bold", 10))
label_1.place(x=80,y=270)
list1 = ['First','Second','Third','Fourth'];

droplist=OptionMenu(root,dept, *list1)
droplist.config(width=15)
dept.set('Select Year')
droplist.place(x=240,y=265)


label_3 = Label(root, text="Gender",bg="#123C69",fg="#FFFFFF",width=20,font=("bold", 10))
label_3.place(x=70,y=300)

R1=Radiobutton(root, text="Male",padx = 5,bg="#123C69",variable=var, value=1).place(x=235,y=300)

R2=Radiobutton(root, text="Female",padx = 20,bg="#123C69",variable=var, value=2).place(x=290,y=300)

label_4 = Label(root, text="Enter Address",bg="#123C69",fg="#FFFFFF",width=20,font=("bold", 10))
label_4.place(x=80,y=330)

entry_4 = Entry(root,textvar=address)
entry_4.place(x=240,y=330)

label_4 = Label(root, text="Enter Birth Date",bg="#123C69",fg="#FFFFFF",width=20,font=("bold", 10))
label_4.place(x=80,y=360)

entry_4 = Entry(root,textvar=dob)
entry_4.place(x=240,y=360)



Button(root, text='Next',width=20,bg='#FCCD04',fg='black',command=validate).place(x=180,y=390)

root.mainloop()
