from tkinter import *

root = Tk()
root.title("Calculator")

def clickMe():
    if e.get() != IntVar and e2.get() != IntVar:
        Label(root, text="\tOne/More Fields are empty !!").grid(row=3, column=0)
    else:
        Label(root, text=int(e.get()) + int(e2.get())).grid(row=3, column=1)

Label(root, text="Enter First Number : ").grid(row=0, column=0)
e = Entry(root, width=20, border=5)
e.grid(row=0, column=1)

Label(root, text="Enter Second Number : ").grid(row=1, column=0)
e2 = Entry(root, width=20, border=5)
e2.grid(row=1, column=1)

Button(root, text="Add", command=clickMe, fg="White", bg="Green").grid(row=2, column=0)
Button(root, text="Quit Me", command=root.destroy, bg="Red", fg="White").grid(row=2, column=1)


root.mainloop()