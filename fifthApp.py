from tkinter import *
from PIL import ImageTk, Image

root = Tk()

img = Image.open("CALC.jpg")
# img = img.resize(500, 500)
 
myImg = ImageTk.PhotoImage(img)

Label(image=myImg).pack()


root.mainloop()