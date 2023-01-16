from tkinter import *
from tkinter import ttk


class Window:
    @staticmethod
    def createWindow():
        root = Tk()
        frame = ttk.Frame(root, padding=10)
        frame.grid()

        return root, frame

    def __init__(self):
        self.root, self.frame = Window.createWindow()

        self.createLabels()
        self.createButtons()
        self.createInputs()

        self.root.mainloop()

    def createLabels(self):
        pass

    def createButtons(self):
        pass

    def createInputs(self):
        pass
