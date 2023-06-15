from tkinter import *

root = Tk()

def greet():
    Label(root, text="Hello World", padx=20, pady=20, font="Helvetica 20 bold italic", fg="Black", bg="Red").grid(row=0, column=1)


userName = StringVar()

Button(root, text="Click Me", command=greet, padx=20, pady=20, border=5, bg="green", fg="Blue").grid(row=1, column=0)

Button(root, text="Quit Me", command=root.destroy, padx=20, pady=20, border=5, bg="red", fg="black").grid(row=1, column=2)

root.mainloop()