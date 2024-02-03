from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image

root = Tk()
root.title('My First window')
root.iconbitmap('C:/Users/mohbc/OneDrive/Documents/good/Tkinter/codemy.ico')

def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir="C:/Users/mohbc/OneDrive/Documents/good/Tkinter/images", title="Select a file", filetypes=(("jpg files", "*.jpg"), ("all files", "*.*")))
    my_label = Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()

my_btn = Button(root, text="Open File", command=open).pack()

root.mainloop()