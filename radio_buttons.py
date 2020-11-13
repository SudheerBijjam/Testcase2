from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Simple image")
root.iconbitmap("C:/Users/sudhe/PycharmProjects/pythonProject/hi.ico")

pizza = StringVar()
pizza.set("pepparoni")
toppings =[("pepparoni", "pepparoni"),
    ("cheese", "cheese"),
    ("tomato", "tomato"),
    ("onion", "onion")]
for text, topping in toppings:
    Radiobutton(root, text=text, variable=pizza, value=topping, command=lambda: click(pizza.get())).pack()

def click(value):
    mylabel = Label(root, text=value)
    mylabel.pack()


mainloop()
