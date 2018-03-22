from tkinter import *
from Classes import Helpers

COUNTER = 0
def counter_label(LABEL):
    def count():
        global COUNTER
        COUNTER = COUNTER + 1
        LABEL.config(text=str(COUNTER))
        LABEL.after(1000, count)
    count()

ROOT = Helpers.TkHelper.GetTk()

ROOT.title("Načítání číslených hodnot")
LABEL = Label(ROOT, fg="red", width=30)
LABEL.pack()
counter_label(LABEL)

ROOT.mainloop()