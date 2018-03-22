from tkinter import *
from Classes import Helpers

class App:
    def __init__(self, master):
        self.__frame = Frame(master)
        self.__frame.pack()
        
        self.__button = Button(self.__frame, text="Quit", command=self.__frame.quit)
        self.__button.pack(side = LEFT)

ROOT = Helpers.TkHelper.GetTk()

APP = App(ROOT)

ROOT.mainloop()