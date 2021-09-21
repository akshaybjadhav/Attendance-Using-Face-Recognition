from tkinter import *
import sqlite3
import os
import argparse
ap = argparse.ArgumentParser()
ap.add_argument("-m", "--id", required=True,
	help="path to trained model")
args = vars(ap.parse_args())
rpk=args["id"]
print(args["id"]+"kkkkkkkkkkkkkkk")

def popupmsg(msg):
   popup=Tk()
   popup.wm_title("Message")
   popup.resizable(0,0)
   label=Label(popup,text=msg,width=30,font=("bold", 10))
   label.pack(side="top",fill="x",pady=10)
   B1=Button(popup,text="OK",command=popup.destroy)
   B1.pack()
   popup.mainloop()

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

   if (var.get() != 0):
      check = check + 1
   else:
      popupmsg("Enter Gender")

   if (address.get() != ""):
      check = check + 1
   else:
      popupmsg("Enter Address")

   if (dept.get() != "Select Department"):
      check = check + 1
   else:
      popupmsg("Select Department")

   if (dob.get() != ""):
      check = check + 1
   else:
      popupmsg("Enter DOB")
   if(check==9):
      update()


def home():
   root.destroy()
   os.system('admin_home1.py')

def logout():
   root.destroy()
   os.system('home.py')




def update():
   name1=fname.get()
   name2=mname.get()
   name3=lname.get()
   address1=address.get()
   gender1=var.get()
   dept1=dept.get()
   email1=email.get()
   contact1=contact.get()
   dob1=dob.get()

   if(gender1==1):
      gender='male'
   elif(gender1==2):
      gender='female'

   conn = sqlite3.connect('Form1.db')
   with conn:
      cursor = conn.cursor()
   oldid = int(rpk)
   if (dept1==dept2):
      newid=oldid
   else:
      cursor.execute('Select MAX(id) from student where dept =?', (dept1,))
      rslt = cursor.fetchone()
      maxid = rslt[0]
      if maxid == None:
         if dept1 == 'First': branch = 100
         if dept1 == 'Second': branch = 200
         if dept1 == 'Third': branch = 300
         if dept1 == 'Fourth': branch = 400
         newid = branch + 1
      else:
         newid = maxid + 1
      path = 'Faces'
      sampleNum = 0
      imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
      for imagePath in imagePaths:
         userID = int(os.path.split(imagePath)[-1].split('.')[1])
         if (oldid == userID):
            sampleNum = sampleNum + 1
            os.rename(imagePath, "Faces/User."+str(newid)+"." + str(sampleNum) + ".jpg")

   cursor.execute('update student SET id=?,fname=?,mname=?,lname=?,contact=?,email=?,gender=?,address=?,dept=?,dob=? Where id=?',(newid,name1,name2,name3,contact1,email1,gender,address1,dept1,dob1,oldid))
   conn.commit()
   conn.close()
   root.destroy()
   msg = "Record updated succefully\n Please note your id:" + str(newid) +"\nClick OK to train data"
   popupmsg(msg)
   os.system('trainer.py')


root = Tk()
ws= root.winfo_screenwidth()
hs=root.winfo_screenheight()
x=(ws/2)-250
y=(hs/2)-250
root.geometry('%dx%d+%d+%d' % (500, 500, x, y))
root.title("ATTENDANCE VIA FACE RECOGNITION SYSTEM")
root.configure(background="#123C69")
root.resizable(0,0)

id=IntVar()
fname=StringVar()
mname=StringVar()
lname=StringVar()
email=StringVar()
address=StringVar()
var = IntVar()
contact=StringVar()
dept=StringVar()
dob=StringVar()
address=StringVar()

#first row
label_0 = Label(root, text="ATTENDANCE SYSTEM",bg="#123C69",fg="#FFFFFF", width=30,font=("Algerian", 20))
label_0.place(x=15,y=13)
Button(root, text='Home',width=15,height=1,bg='#FCCD04',fg='black',command=home).place(x=0,y=51)
label_1 = Label(root, text="Student Record Update Form",bg="#FCCD04",width=33,height=1,font=("bold", 10))
label_1.place(x=118,y=51)
Button(root, text='Logout',width=15,bg='#FCCD04',height=1,fg='black',command=logout).place(x=391,y=51)
label_0 = Label(root, text="All fileds are Mandatory",bg="#123C69",fg="#FFFFFF",width=20,font=("bold", 10))
label_0.place(x=160,y=90)

label_fname = Label(root, text="First Name",bg="#123C69",fg="#FFFFFF",width=20,font=("bold", 10))
label_fname.place(x=80,y=120)
entry_fname = Entry(root,textvar=fname)
entry_fname.place(x=240,y=120)
label_mname = Label(root, text="Middle Name",bg="#123C69",fg="#FFFFFF",width=20,font=("bold", 10))
label_mname.place(x=80,y=150)
entry_mname = Entry(root,textvar=mname)
entry_mname.place(x=240,y=150)
label_lname = Label(root, text="Last Name",bg="#123C69",fg="#FFFFFF",width=20,font=("bold", 10))
label_lname.place(x=80,y=180)
entry_lname = Entry(root,textvar=lname)
entry_lname.place(x=240,y=180)
label_contact = Label(root, text="Contact",bg="#123C69",fg="#FFFFFF",width=20,font=("bold", 10))
label_contact.place(x=80,y=210)
entry_contact = Entry(root,textvar=contact)
entry_contact.place(x=240,y=210)
label_email = Label(root, text="Email",bg="#123C69",fg="#FFFFFF",width=20,font=("bold", 10))
label_email.place(x=80,y=240)
entry_email = Entry(root,textvar=email)
entry_email.place(x=240,y=240)
label_7editor = Label(root, text="Gender",bg="#123C69",fg="#FFFFFF",width=20,font=("bold", 10))
label_7editor.place(x=80,y=270)
R1=Radiobutton(root, text="Male",padx = 5,bg="#123C69", variable=var, value=1).place(x=235,y=270)
R2=Radiobutton(root, text="Female",padx = 20,bg="#123C69", variable=var, value=2).place(x=290,y=270)
label_address = Label(root, text="Address",bg="#123C69",fg="#FFFFFF",width=20,font=("bold", 10))
label_address.place(x=80,y=300)
entry_address = Entry(root,textvar=address)
entry_address.place(x=240,y=300)

label_1 = Label(root, text="Department",bg="#123C69",fg="#FFFFFF",width=20,font=("bold", 10))
label_1.place(x=80,y=330)
list1 = ['First','Second','Third','Fourth'];
droplist=OptionMenu(root,dept, *list1)
droplist.config(width=15)
dept.set('Select Year')
droplist.place(x=240,y=325)

label_dob = Label(root, text="Birth Date",bg="#123C69",fg="#FFFFFF",width=20,font=("bold", 10))
label_dob.place(x=80,y=360)
entry_dob = Entry(root,textvar=dob)
entry_dob.place(x=240,y=360)


conn = sqlite3.connect('Form1.db')
c=conn.cursor()
c.execute('SELECT * FROM student WHERE id=?',(str(rpk),))
records=c.fetchall()

for record in records:

   entry_fname.insert(0,record[1])
   entry_mname.insert(0,record[2])
   entry_lname.insert(0,record[3])
   entry_contact.insert(0,record[4])
   entry_email.insert(0,record[5])
   if(record[6]=="male"):var.set(1)
   if (record[6] =="female"):var.set(2)
   entry_address.insert(0,record[7])
   dept.set(record[8])
   dept2=record[8]
   entry_dob.insert(0,record[9])


B3=Button(root, text='SAVE & UPDATE',width=20,bg='#FCCD04',fg='black',command=validate).place(x=180,y=410)


root.mainloop()
