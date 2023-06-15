from tkinter import *

root = Tk()
root.title("First Code")

# Label(root, text="Hello World", padx=10, pady=90, font="Helvetica 59 bold italic", background="black", foreground="white").pack(side="left", fill="both")

Label(root, text="Hello World", padx=10, pady=90, font="Helvetica 59 bold italic", background="white", foreground="black").grid(row=0, column=0)

Label(root, text="Hello World", padx=10, pady=90, font="Helvetica 59 bold italic", background="black", foreground="white").grid(row=0, column=1)

Label(root, text="Hello World", padx=10, pady=90, font="Helvetica 59 bold italic", background="black", foreground="white").grid(row=1, column=0)

Label(root, text="Hello World", padx=10, pady=90, font="Helvetica 59 bold italic", background="white", foreground="black").grid(row=1, column=1)

Label(root, text="Hello World", padx=10, pady=90, font="Helvetica 59 bold italic", background="white", foreground="black").grid(row=2, column=0)

Label(root, text="Hello World", padx=10, pady=90, font="Helvetica 59 bold italic", background="black", foreground="white").grid(row=2, column=1)

root.mainloop()