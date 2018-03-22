from tkinter import Tk

class TkHelper():
    @staticmethod
    def GetTk():
        ROOT = Tk()
        ROOT.minsize(450, 250)
        return ROOT