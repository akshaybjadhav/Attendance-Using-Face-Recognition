from tkinter import *
import os
from PIL import ImageTk, Image

root = Tk()
root.geometry('870x500')
root.title("ATTENDANCE VIA FACE RECOGNITION SYSTEM")
root.configure(background="#123C69")
root.resizable(0, 0)

uname = StringVar()
pwd = StringVar()


def run1():
    root.destroy()
    os.system('students_details.py')


def run2():
    root.destroy()
    os.system('view_details.py')


def run3():
    root.destroy()
    os.system('enter_ID.py')


def run4():
    root.destroy()
    os.system('ID_delete.py')

def run5():
    root.destroy()
    os.system('home.py')

def run6():
    root.destroy()
    os.system('student_recognition.py')

def run7():
    root.destroy()
    os.system('add_notice.py')

def run8():
    root.destroy()
    os.system('view_attendance1.py')

def run9():
    root.destroy()
    os.system('view_notice1.py')



label_2 = Label(root, text="ATTENDANCE SYSTEM", width=50, font=("Algerian", 20), fg="#FFFFFF", bg="#123C69")
label_2.place(x=15, y=15)

label_0 = Label(root, text="ADMIN HOME PAGE", width=108, font=("bold", 10), fg="#FFFFFF", bg="#aa4433")
label_0.place(x=1, y=50)


# label_1 = Label(root, text="UserName",width=20,font=("bold", 10))
# label_1.place(x=80,y=130)

# entry_1 = Entry(root,textvar=uname)
# entry_1.place(x=240,y=130)


# label_4 = Label(root, text="Programming",width=20,font=("bold", 10))
# label_4.place(x=85,y=330)
# var2= IntVar()
# Checkbutton(root, text="java", variable=var1).place(x=235,y=330)
# Checkbutton(root, text="python", variable=var2).place(x=290,y=330)
Button(root, text='ADD STUDENT', width=13, bg='#FCCD04', fg='black', command=run1).place(x=1, y=73)

Button(root, text='VIEW STUDENT', width=13, bg='#FCCD04', fg='black', command=run2).place(x=103, y=73)

Button(root, text='UPDATE', width=10, bg='#FCCD04', fg='black', command=run3).place(x=205, y=73)

Button(root, text='DELETE', width=10, bg='#FCCD04', fg='black', command=run4).place(x=286, y=73)

Button(root, text='START', width=10, bg='#FCCD04', fg='black', command=run6).place(x=367, y=73)

Button(root, text='ADD NOTICE', width=13, bg='#FCCD04', fg='black', command=run7).place(x=448, y=73)

Button(root, text='VIEW NOTICE', width=13, bg='#FCCD04', fg='black', command=run9).place(x=550, y=73)

Button(root, text='VIEW ATTENDANCE', width=15, bg='#FCCD04', fg='black', command=run8).place(x=652, y=73)

Button(root, text='LOGOUT', width=13, bg='#FCCD04', fg='black', command=run5).place(x=768, y=73)

path = "i1.jpg"

# Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(Image.open(path))

# The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = Label(root, image=img, bg="#123C69")
panel.config(width=1000)
panel.config(height=300)
panel.config(anchor="center")
#panel.place(x=150,y=160)

# The Pack geometry manager packs widgets in rows or columns.
panel.pack(side="left", anchor="center")  # side = "up", fill = "both", expand = "yes")

root.mainloop()
