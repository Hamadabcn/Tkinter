from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('HamadaBCN developers')
root.iconbitmap('C:/Users/mohbc/OneDrive/Documents/good/Tkinter/codemy.ico')

#r = IntVar()
#r.set("2")

TOPPINGS = [
    ("Cuatro quesos", "Cuatro quesos"),
    ("Margerita", "Matgerita"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion"),
    ("Marinera", "Marinera"),
    ("Queso y trufa", "Queso y trufa"),
]  


pizza = StringVar()
pizza.set("Cuatro quesos")

for text, topping in TOPPINGS:
    Radiobutton(root, text=text, variable=pizza, value=topping).pack(anchor=W)

def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()

#Radiobutton(root, text="eat", variable=r, value=1, command=lambda: clicked(r.get())).pack()
#Radiobutton(root, text="sleep", variable=r, value=2, command=lambda: clicked(r.get())).pack()
#Radiobutton(root, text="code", variable=r, value=3, command=lambda: clicked(r.get())).pack()
#Radiobutton(root, text="repeat", variable=r, value=4, command=lambda: clicked(r.get())).pack()

#myLabel = Label(root, text=pizza.get())
#myLabel.pack()

myButton = Button(root, text="Click here!", command=lambda: clicked(pizza.get()))
myButton.pack()
root.mainloop()