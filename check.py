from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Hamadabcn Software Development')
root.iconbitmap('C:/Users/mohbc/OneDrive/Documents/good/Tkinter/codemy.ico')
root.geometry("400x400")

def show():
    my_label = Label(root, text=var.get()).pack()

var = StringVar()

c = Checkbutton(root, text="Check this box", variable=var, onvalue="On", offvalue="Off")
c.deselect()
c.pack()

my_button = Button(root, text="Show selection", command=show).pack()

root.mainloop()