from tkinter import *
import os
from PIL import ImageTk, Image

root = Tk()
ws= root.winfo_screenwidth()
hs=root.winfo_screenheight()
x=(ws/2)-250
y=(hs/2)-250
root.geometry('%dx%d+%d+%d' % (510, 510, x, y))
root.title("ATTENDANCE VIA FACE RECOGNITION SYSTEM")
root.configure(background="#123C69")
root.resizable(0,0)

def run1():
    root.destroy()
    os.system('student_login.py')


def run3():
    root.destroy()
    os.system('admin_login.py')

def run4():
    root.destroy()
    os.system('recognition-covid.py')

    


#first row
label_01 = Label(root, text="ATTENDANCE SYSTEM",bg="#123C69",fg="#FFFFFF", width=30,font=("Algerian", 20))
label_01.place(x=15,y=13)

label_11 = Label(root, text="Attendance System Home Page",bg="#FCCD04",width=65,height=1,font=("bold", 10))
label_11.place(x=0,y=75)


Button(root, text='STUDENT LOGIN',width=22,bg='#E9B000',fg='black',command=run1).place(x=90,y=430)
Button(root, text='ADMIN LOGIN',width=22,bg='#E9B000',fg='black',command=run3).place(x=255,y=430)
#Button(root, text='TAKE ATTENDANCE',width=21,bg='#E9B000',fg='black',command=run4).place(x=266,y=430)


path = "i1.jpg"

#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(Image.open(path))

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = Label(root, image = img,bg="#123C69")
panel.config( width=500 )
panel.config( height=300 )
panel.config( anchor="center" )
#panel.place(x=150,y=160)

#The Pack geometry manager packs widgets in rows or columns.
panel.pack(side = "left",anchor="center")#side = "up", fill = "both", expand = "yes")


root.mainloop()
