from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('HamadaBCN developers')
root.iconbitmap('C:/Users/mohbc/OneDrive/Documents/good/Tkinter/codemy.ico')

frame = LabelFrame(root, padx=50, pady=50)
frame.pack(padx=100, pady=100)

b = Button(frame, text="don't you ever click me!❌")
b2= Button(frame, text="or here...❌")
b.grid(row=0, column=0)
b2.grid(row=1, column=1)

root.mainloop()