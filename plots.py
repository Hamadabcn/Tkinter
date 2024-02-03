from tkinter import *
from PIL import ImageTk,Image
import numpy as np
import matplotlib.pyplot as plt


root = Tk()
root.title('Hamadabcn Software Development')
root.iconbitmap('C:/Users/mohbc/OneDrive/Documents/good/Tkinter/codemy.ico')
root.geometry("400x200")

def graph():
    house_prices = np.random.normal(200000, 25000, 5000)
    
    # different graphs plots
    #plt.hist(house_prices, 200)
    #plt.pie(house_prices)
    #plt.plot(house_prices)
    plt.polar(house_prices)
    plt.show()
    
my_button = Button(root, text="Graphs", command=graph)
my_button.pack()

root.mainloop()