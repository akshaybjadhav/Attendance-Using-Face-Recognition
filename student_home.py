from tkinter import *
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
root.resizable(0, 0)

uname = StringVar()
pwd = StringVar()


def run1():
    root.destroy()
    os.system('student_home.py')


def run2():
    root.destroy()
    os.system('view_attendance.py')


def run3():
    root.destroy()
    os.system('view_notice.py')


def run4():
    root.destroy()
    os.system('home.py')




label_2 = Label(root, text="ATTENDANCE SYSTEM", width=30, font=("Algerian", 20), fg="#FFFFFF", bg="#123C69")
label_2.place(x=15, y=15)

label_0 = Label(root, text="STUDENT HOME PAGE", width=65, font=("bold", 10), fg="#FFFFFF", bg="#aa4433")
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



Button(root, text='HOME', width=19, bg='#FCCD04', fg='black', command=run1).place(x=1, y=73)

Button(root, text='ATTENDANCE', width=19, bg='#FCCD04', fg='black', command=run2).place(x=130, y=73)

Button(root, text='NOTICE', width=19, bg='#FCCD04', fg='black', command=run3).place(x=250, y=73)

Button(root, text='LOGOUT', width=19, bg='#FCCD04', fg='black', command=run4).place(x=370, y=73)



path = "i1.jpg"

# Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(Image.open(path))

# The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = Label(root, image=img, bg="#123C69")
panel.config(width=500)
panel.config(height=300)
panel.config(anchor="center")
# panel.place(x=150,y=160)

# The Pack geometry manager packs widgets in rows or columns.
panel.pack(side="left", anchor="center")  # side = "up", fill = "both", expand = "yes")

root.mainloop()
