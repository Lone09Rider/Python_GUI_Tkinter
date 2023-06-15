from tkinter import *
from PIL import ImageTk, Image
import sqlite3
import tkinter.messagebox

root = Tk()
root.geometry("500x650")
root.maxsize(500, 650)
root.minsize(500, 650)

conn = sqlite3.connect("College.db")
cur =  conn.cursor()
# cur.execute("CREATE TABLE person (name TEXT, age INT, gen TEXT, room TEXT, course TEXT)")
# conn.commit()
# conn.close()

def action():
    name = e1.get() 
    age = e2.get()
    gen = gender.get()
    room = listroom.get()
    course1 = ""
    course2 = ""
    if courseCheck1.get() == '1':
        course1 = "Java"
    if courseCheck2.get() == '1':
        course2 = "Python"
    course3 = course1 + " " + course2

    # print(name)
    # print(age)
    # print(gen)
    # print(room)
    # print(course3)

    cur.execute("INSERT INTO person VALUES('"+name+"', '"+age+"', '"+gen+"', '"+room+"', '"+course3+"')")

    tkinter.messagebox.showinfo("Output", "User Data Inserted Successfully !! Congrats.")
    print("Executed Successfully !!")

    conn.commit()
    conn.close()

    e1.delete(0, END)
    e2.delete(0, END)

img = Image.open("student.png")

studImg = ImageTk.PhotoImage(img)
label = Label(image=studImg)
label.place(x=200,y=30)

# root.configure(background="Black")

l1 = Label(root, text="Sign Up for College !!", font="times_new_roman 25 bold", fg="white", bg="black")
l1.place(x=90, y=120)

l2 = Label(root, text="Enter Your Name", font="time 15 bold")
l2.place(x=30, y=220)

e1 = Entry(root, width=30, bd=3)
e1.place(x=280, y=220)

l3 = Label(root, text="Enter Your Age", font="time 15 bold")
l3.place(x=30, y=260)

e2 = Entry(root, width=30, bd=3)
e2.place(x=280, y=260)


l3 = Label(root, text="Select Your Gender", font="time 15 bold")
l3.place(x=30, y=340)

gender = StringVar(root)

g1 = Radiobutton(root, text="Male", variable=gender, value="Male", font="time 15")
g1.select()
g1.place(x=280, y=340)

g2 = Radiobutton(root, text="Female", variable=gender, value="Female", font="time 15")
g2.deselect()
g2.place(x=360, y=340)

l4 = Label(root, text="Select Room", font="time 15 bold")
l4.place(x=30, y=390)

list = ['AC Room', 'Non Ac Room', 'Chai Tapri']
listroom = StringVar(root)
listroom.set("Select Your room Type")

menu = OptionMenu(root, listroom, *list)
menu.place(x=280, y=390, width=190)

l5 = Label(root, text="Select Course", font="time 15 bold")
l5.place(x=30, y=440)

courseCheck1 = StringVar(root)
courseCheck2 = StringVar(root)


courseBox1 = Checkbutton(root, text="Java", variable=courseCheck1)
courseBox1.place(x = 280, y=440)
courseBox1.deselect()


courseBox2 = Checkbutton(root, text="Python", variable=courseCheck2)
courseBox2.place(x = 360, y=440)
courseBox2.deselect()

button1 = Button(root, text="Submit", padx=200, pady=10, bg="Blue", fg="White", font="time 10 bold", command=action)
button1.place(x=30, y= 510)

button2 = Button(root, text="Quit", padx=210, pady=10, command=root.quit, bg="Red", fg="White", font="time 10 bold")
button2.place(x=30, y= 570)

root.mainloop()
