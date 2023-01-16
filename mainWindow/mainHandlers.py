from genTokenWindow.GenTokenWindow import GenTokenWindow
from tkinter import filedialog
from core.window import Window
from tkinter.messagebox import showwarning, showinfo
from API.Telegraph import telegraph_instance

from core.utils import *
from tkinter import ttk


def getCreateErrorMessage():
    if not telegraph_instance.isTokenCreated() and not telegraph_instance.isDirChoosen():
        return "Вы не указали токен и папку!"
    elif not telegraph_instance.isTokenCreated():
        return "Вы не указали токен"
    elif not telegraph_instance.isDirChoosen():
        return "Вы не указали папку"
    else:
        return False

class MainWindowHandlers:
    @staticmethod
    def genToken(onTokenGenerated):
        if not telegraph_instance.isTokenCreated():
            GenTokenWindow(lambda: onTokenGenerated(telegraph_instance.access_token))
        else:
            showwarning(message="Токен уже создан!")

    @staticmethod
    def done():
        if getCreateErrorMessage():
            showwarning(message=getCreateErrorMessage())
            return True

        showinfo(message="Идёт загрузка")

        link = telegraph_instance.createPage()

        if not link:
            return False

        localRoot, doneFrm = Window.createWindow()

        ttk.Label(doneFrm, text="Ссылка: {}".format(link)).grid(column=0, row=0)
        ttk.Button(doneFrm, text="Скопировать", command=lambda: copy2clip(link) or localRoot.destroy()).grid(column=1, row=0)

        return True

    @staticmethod
    def chooseDir():
        dirPath = filedialog.askdirectory()
        telegraph_instance.setImageDir(dirPath)

        return dirPath

    @staticmethod
    def handleWriteToken(newToken):
        telegraph_instance.setToken(newToken)
