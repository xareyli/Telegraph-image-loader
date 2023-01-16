from API.Telegraph import telegraph_instance
from core.window import Window
from core.utils import *

from tkinter import ttk


class GenTokenWindowHandlers:
    @staticmethod
    def doneHandler(accountName, authorName):
        account = telegraph_instance.createAccount(accountName, authorName)

        root, frame = Window.createWindow()

        ttk.Label(frame,
                  text="Перейдите по этой ссылке в браузере, чтобы иметь возможность редактировать будущую статью").grid(
            column=0, row=0)
        ttk.Label(frame, text="Ссылка: {}".format(account['auth_url'])).grid(column=0, row=1)
        ttk.Button(frame, text="Скопировать", command=lambda: GenTokenWindowHandlers.handleCopyAuthUrl(account, root)).grid(column=1, row=1)

    @staticmethod
    def handleCopyAuthUrl(account, root):
        copy2clip(account['auth_url'])
        root.destroy()
