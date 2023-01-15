from tkinter import *
from tkinter import ttk


def createWindow():
    root = Tk()
    frame = ttk.Frame(localRoot, padding=10)
    frame.grid()

    return  root, frame
