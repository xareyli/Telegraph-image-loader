from core.window import *
from tkinter import *
from tkinter import ttk
from API.Telegraph import telegraph_instance

from tkinter.messagebox import showwarning
from mainWindow.mainHandlers import MainWindowHandlers


class MainWindow(Window):
    root = None
    frame = None

    dirLabel = None

    tokenInput = None
    tokenInputSV = None

    def _genTokenHandler(self):
        MainWindowHandlers.genToken(lambda token: self.tokenInputSV.set(token))

    def _doneHandler(self):
        isSuccess = MainWindowHandlers.done()

        if not isSuccess:
            showwarning(message="Неверный токен")

    def _chooseDirHandler(self):
        dirPath = MainWindowHandlers.chooseDir()

        self.dirLabel.config(text=dirPath)

    def _handleWriteToken(self):
        MainWindowHandlers.handleWriteToken(self.tokenInputSV.get())

    def createLabels(self):
        ttk.Label(self.frame, text="Токен доступа").grid(column=1, row=0)
        ttk.Label(self.frame, text="Made by Xareyli (telegram: @xareyli)").grid(column=1, row=5)
        self.dirLabel = ttk.Label(self.frame, text="Папка не выбрана")
        self.dirLabel.grid(column=1, row=3)

    def createButtons(self):
        ttk.Button(self.frame, text="Создать токен", command=self._genTokenHandler).grid(column=0, row=1)
        ttk.Button(self.frame, text="Загрузить", command=self._doneHandler).grid(column=0, row=2)
        ttk.Button(self.frame, text="Выбрать папку", command=self._chooseDirHandler).grid(column=0, row=3)

    def createInputs(self):
        self.tokenInputSV = StringVar()
        self.tokenInputSV.trace("w", lambda name, index, mode, sv=self.tokenInputSV: self._handleWriteToken())

        self.tokenInput = ttk.Entry(self.frame, textvariable=self.tokenInputSV)
        self.tokenInput.grid(column=1, row=1)
