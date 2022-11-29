from tkinter import *
from tkinter import messagebox
root = Tk();
root.geometry("400x400")
def click():
    msg = messagebox.showinfo("Message","Hello world")
    button = Button(root,text="Message button",command=click).pack();
  
    root.mainloop();