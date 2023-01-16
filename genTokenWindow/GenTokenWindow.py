from core.window import *
from tkinter import ttk
from genTokenWindow.genTokenHandlers import GenTokenWindowHandlers


class GenTokenWindow(Window):
    accountInput = None
    authorInput = None
    onTokenGenerated = None

    def __init__(self, onTokenGenerated):
        self.onTokenGenerated = onTokenGenerated

        super().__init__()

    def _handleDone(self):
        GenTokenWindowHandlers.doneHandler(self.accountInput.get(), self.authorInput.get())
        self.onTokenGenerated()
        self.root.destroy()

    def createLabels(self):
        ttk.Label(self.frame, text="Имя аккаунта").grid(column=0, row=0)
        ttk.Label(self.frame, text="Имя автора").grid(column=0, row=1)

    def createButtons(self):
        ttk.Button(self.frame, text="Подтвердить", command=self._handleDone).grid(column=0, row=2)

    def createInputs(self):
        self.accountInput = ttk.Entry(self.frame)
        self.accountInput.grid(column=1, row=0)

        self.authorInput = ttk.Entry(self.frame)
        self.authorInput.grid(column=1, row=1)
