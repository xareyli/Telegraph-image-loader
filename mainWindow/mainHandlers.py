from genTokenWindow.GenTokenWindow import GenTokenWindow
from tkinter import filedialog
from core.window import Window
from tkinter.messagebox import showwarning
from API.Telegraph import telegraph_instance

from core.utils import *
from tkinter import ttk


class MainWindowHandlers:
    @staticmethod
    def genToken(onTokenGenerated):
        if not telegraph_instance.isTokenCreated():
            GenTokenWindow(lambda: onTokenGenerated(telegraph_instance.access_token))
        else:
            showwarning(message="Токен уже создан!")

    @staticmethod
    def done():
        link = telegraph_instance.createPage()

        localRoot, doneFrm = Window.createWindow()

        ttk.Label(doneFrm, text="Ссылка: {}".format(link)).grid(column=0, row=0)
        ttk.Button(doneFrm, text="Скопировать", command=lambda: copy2clip(link) or localRoot.destroy()).grid(column=1, row=0)

    @staticmethod
    def chooseDir():
        dirPath = filedialog.askdirectory()
        telegraph_instance.setImageDir(dirPath)

        return dirPath

    @staticmethod
    def handleWriteToken(newToken):
        telegraph_instance.setToken(newToken)
