from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Hamadabcn Software Development')
root.iconbitmap('C:/Users/mohbc/OneDrive/Documents/good/Tkinter/codemy.ico')
root.geometry("400x400")

def show():
    my_label = Label(root, text=clicked.get()).pack()

options = [
    "Monday", 
    "Tuesday", 
    "Wednesday", 
    "Thursday", 
    "Friday", 
    "Saturday", 
    "Sunday",
]    

# drop down boxes
clicked = StringVar()
clicked.set(options[0])    

# The line `drop = OptionMenu(root, clicked, "Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
# "Saturday", "Sunday")` creates a drop-down menu (also known as an OptionMenu) in the tkinter window.
drop = OptionMenu(root, clicked, *options)
drop.pack()

my_button = Button(root, text="Show Selection", command=show).pack()

root.mainloop()