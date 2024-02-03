from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('My First window')
root.iconbitmap('C:/Users/mohbc/OneDrive/Documents/good/Tkinter/codemy.ico')

def open():
    global my_image
    top = Toplevel()
    top.title('My Second window')
    top.iconbitmap('C:/Users/mohbc/OneDrive/Documents/good/Tkinter/codemy.ico')
    my_image = ImageTk.PhotoImage(Image.open("images/aspen.png"))
    my_label = Label(top, image=my_image).pack()
    
    btn2 = Button(top, text="Close window", command=top.destroy).pack()

btn = Button(root, text="Open second window", command=open).pack()

root.mainloop()