from tkinter import *

root = Tk()

# creating a label widget
myLabel1 = Label(root, text="Hello world!").grid(row=0, column=0) # another way to do it
myLabel2 = Label(root, text="My name is Hamada!").grid(row=1, column=5)

# we are putting it on the screen
#myLabel1.grid(row=0, column=0)
#myLabel2.grid(row=1, column=5)

root.mainloop()
