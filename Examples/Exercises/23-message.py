from tkinter import *
from Classes import Helpers

ROOT = Helpers.TkHelper.GetTk()

MESSAGE = Message(ROOT, text="Test message")
MESSAGE.config(width=100, font=24)
MESSAGE.pack()

ROOT.mainloop()