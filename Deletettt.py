from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

popup = Tk()
popup.wm_title("!")


ws= popup.winfo_screenwidth()
hs=popup.winfo_screenheight()
x=(ws/2)-250
y=(hs/2)-250
popup.geometry('%dx%d+%d+%d' % (0, 0, x, y))

popup.resizable(0, 0)
label = Label(popup, text="msg", width=30, font=("bold", 10))
label.pack(side="top", fill="x", pady=10)
B1 = Button(popup, text="OK", command=popup.destroy)
B1.pack()
popup.mainloop()


#root = Tk()
#root.title("Title")
#root.geometry('600x600')

#def resize_image(event):
 #   image = copy_of_image.resize((root.winfo_width(),root.winfo_height()))
  #  photo = ImageTk.PhotoImage(image)
   # label.config(image = photo)
    #label.image = photo #avoid garbage collection

#image = Image.open(r"C:\Users\Akshay\Pictures\captured1.png")
#copy_of_image = image.copy()
#photo = ImageTk.PhotoImage(image)
#label = ttk.Label(root, image = photo)
#label.bind('<Configure>', resize_image)
#label.pack(fill=BOTH, expand = YES)

#root.mainloop()'''