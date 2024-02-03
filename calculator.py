from tkinter import *
from PIL import ImageTk, Image

root = Tk()

root.title("Hamadabcn Calculator App ")
root.iconbitmap("C:/Users/mohbc/OneDrive/Documents/good/Tkinter/codemy.ico")

e = Entry(root, width=45, borderwidth=5, font=('sans-serif', 11))
#e.insert(0, "Enter your Name: ")
e.grid(row=0, column=0, columnspan=3, padx=10, pady=13)

def button_click(number):
    #e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
    
def button_clear():
    e.delete(0, END)
    
def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, float(f_num) + float(second_number))

    if math == "subtraction":
        e.insert(0, float(f_num) - float(second_number))

    if math == "multiplication":
        e.insert(0, float(f_num) * float(second_number))

    if math == "division":
        e.insert(0, float(f_num) / float(second_number))
        
def button_add():
    first_number = e.get()
    global f_num 
    global math
    math = "addition"
    f_num = float(first_number)  # Change this line
    e.delete(0, END)

def button_subtract():
    first_number = e.get()
    global f_num 
    global math
    math = "subtraction"
    f_num = float(first_number)  # And this line
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    global f_num 
    global math
    math = "multiplication"
    f_num = float(first_number)  # And this one
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num 
    global math
    math = "division"
    f_num = float(first_number)  # And this one too
    e.delete(0, END)
    
def button_click(number):
    current = e.get()
    if "." in current and number == ".":
        pass  # Ignore the decimal point if there's already one
    else:
        e.delete(0, END)
        if current:
            e.insert(0, current + str(number))
        else:
            e.insert(0, str(number))
        
def button_percent():
    global f_num
    second_number = e.get()
    e.delete(0, END)
    e.insert(0, f_num * float(second_number) / 100)

def button_erase():
    current = e.get()
    if current:
        e.delete(len(current) - 1, END)

# define buttons
button_1 = Button(root, text="1", padx=59, pady=25, command=lambda: button_click(1),fg='black')
button_2 = Button(root, text="2", padx=59, pady=25, command=lambda: button_click(2),fg='black')
button_3 = Button(root, text="3", padx=59, pady=25, command=lambda: button_click(3),fg='black')
button_4 = Button(root, text="4", padx=59, pady=25, command=lambda: button_click(4),fg='black')
button_5 = Button(root, text="5", padx=59, pady=25, command=lambda: button_click(5),fg='black')
button_6 = Button(root, text="6", padx=59, pady=25, command=lambda: button_click(6),fg='black')
button_7 = Button(root, text="7", padx=59, pady=25, command=lambda: button_click(7),fg='black')
button_8 = Button(root, text="8", padx=59, pady=25, command=lambda: button_click(8),fg='black')
button_9 = Button(root, text="9", padx=59, pady=25, command=lambda: button_click(9),fg='black')
button_0 = Button(root, text="0", padx=59, pady=25, command=lambda: button_click(0),fg='black')
button_add = Button(root, text="+", padx=58, pady=25, command=button_add, fg='green')
button_equal = Button(root, text="=", padx=59, pady=25, command=button_equal, fg='green')
button_clear = Button(root, text="C", padx=58, pady=25, command=button_clear, fg='red')

button_subtract = Button(root, text="-", padx=60, pady=25, command=button_subtract, fg='green')
button_multiply = Button(root, text="×", padx=59, pady=25, command=button_multiply, fg='green')
button_divide = Button(root, text="÷", padx=59, pady=25, command=button_divide, fg='green')

button_decimal = Button(root, text=".", padx=62, pady=25, command=lambda: button_click("."), fg='black')
button_percent = Button(root, text="%", padx=59, pady=25, command=button_percent, fg='black')

button_erase = Button(root, text="⌫", padx=190, pady=25, command=button_erase, fg='red')


# put buttons on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=2, columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=2, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

button_decimal.grid(row=4, column=1)
button_percent.grid(row=5, column=1)

button_erase.grid(row=7, column=0, columnspan=3)


root.mainloop()
