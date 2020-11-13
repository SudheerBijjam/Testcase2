from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Simple image")
root.iconbitmap("C:/Users/sudhe/PycharmProjects/pythonProject/hi.ico")
root.geometry("400x400")

clicked = StringVar()
clicked.set("Monday")

options = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]



def order():
    label1 =Label(root, text= clicked.get()).pack()


c = OptionMenu(root, clicked, *options)
c.pack()

my_b = Button(root, text = "press it!", command =order).pack()

root.mainloop()
