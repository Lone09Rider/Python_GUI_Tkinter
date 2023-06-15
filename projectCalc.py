from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Calculator")

myImg = ImageTk.PhotoImage(Image.open("CALC.jpg"))

Label(image=myImg).grid(row=7, column=0)

e = Entry(root, width=35, bd=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def Click(num):
    curr = e.get()
    e.delete(0, END)
    e.insert(0, str(curr+num))

def clear():
    e.delete(0, END)

def Add():
    x = int(e.get())
    global fnum
    global math 
    math = 'add'
    fnum = x
    e.delete(0, END)

def sub():
    x = int(e.get())
    global fnum
    global math
    math = 'sub'
    fnum = x
    e.delete(0, END)

def mul():
    x = int(e.get())
    global fnum
    global math
    math = 'mul'
    fnum = x
    e.delete(0, END)


def div():
    x = int(e.get())
    global fnum
    global math
    math = 'div'
    fnum = x
    e.delete(0, END)


def equal():
    y = e.get()
    e.delete(0, END)
    if math == 'add':
        e.insert(0, fnum + int(y))
    if math == "sub":
        e.insert(0, fnum - int(y))
    if math == "mul":
        e.insert(0, fnum * int(y))
    if math == "div":
        e.insert(0, fnum / int(y))

button9 = Button(root, text="9", padx=40, pady=20, border=2, command=lambda: Click("9"))
button9.grid(row=1, column=0)
button8 = Button(root, text="8", padx=40, pady=20, border=2, command=lambda: Click("8"))
button8.grid(row=1, column=1)
button7 = Button(root, text="7", padx=40, pady=20, border=2, command=lambda: Click("7"))
button7.grid(row=1, column=2)
button6 = Button(root, text="6", padx=40, pady=20, border=2, command=lambda: Click("6"))
button6.grid(row=2, column=0)
button5 = Button(root, text="5", padx=40, pady=20, border=2, command=lambda: Click("5"))
button5.grid(row=2, column=1)
button4 = Button(root, text="4", padx=40, pady=20, border=2, command=lambda: Click("4"))
button4.grid(row=2, column=2)
button3 = Button(root, text="3", padx=40, pady=20, border=2, command=lambda: Click("3"))
button3.grid(row=3, column=0)
button2 = Button(root, text="2", padx=40, pady=20, border=2, command=lambda: Click("2"))
button2.grid(row=3, column=1)
button1 = Button(root, text="1", padx=40, pady=20, border=2, command=lambda: Click("1"))
button1.grid(row=3, column=2)
button0 = Button(root, text="0", padx=40, pady=20, border=2, command=lambda: Click("0"))
button0.grid(row=4, column=0)

buttonAdd = Button(root, text="+", padx=40, pady=20, border=2, command=Add)
buttonAdd.grid(row=4, column=1)
buttonSub = Button(root, text="-", padx=40, pady=20, border=2, command=sub)
buttonSub.grid(row=4, column=2)
buttonMul = Button(root, text="*", padx=40, pady=20, border=2, command=mul)
buttonMul.grid(row=5, column=0)
buttonDiv = Button(root, text="/", padx=40, pady=20, border=2, command=div)
buttonDiv.grid(row=5, column=1)
buttonClear= Button(root, text="Clear", padx=40, pady=20, border=2, command=clear)
buttonClear.grid(row=5, column=2)
buttonAns = Button(root, text="=", padx=150, pady=20, border=2, command=equal)
buttonAns.grid(row=6, column=0, columnspan=3)


root.mainloop()