from tkinter import *

def exit():
    sys.exit(0)

root = Tk()

LABEL1 = Label(root, text="Welcome", fg="#4286f4").pack()
BUTTON2 = Button(root, padx=10, text="Close window", bg="#4286f4", command=exit).pack()

root.mainloop()