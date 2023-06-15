from tkinter import *

root = Tk()

def greet():
    Label(root, text=f"Hello, {e.get() or 'World'} !!", bg="black", fg="white", font="Times_New_Roman 20 bold italic").grid(row=2, column=1)

e = Entry(root, width=35, border=10,)
e.grid(row=0, column=1)

Button(root, text="Click Me", command=greet, bg="Green", fg="Black").grid(row=1, column=0)

Button(root, text="Quit Me", command=root.destroy, bg="Red", fg="Black").grid(row=1, column=2)

root.mainloop()