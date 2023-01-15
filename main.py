from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showwarning
from tkinter import filedialog
from lib import *
from utils import *
from window import *


def onButtonClick():
    directoryName = filedialog.askdirectory()


def genToken():
    localRoot, tokenGenFrm = createWindow()

    ttk.Label(tokenGenFrm, text="Имя аккаунта").grid(column=0, row=0)
    ttk.Label(tokenGenFrm, text="Имя автора").grid(column=0, row=1)

    accountInput = ttk.Entry(tokenGenFrm)
    accountInput.grid(column=1, row=0)

    authorInput = ttk.Entry(tokenGenFrm)
    authorInput.grid(column=1, row=1)

    def buttonHandler():
        account = createAccount(accountInput.get(), authorInput.get())
        sv.set(getToken())
        localRoot.destroy()

        accRoot, accFrm = createWindow()

        ttk.Label(accFrm,
                  text="Перейдите по этой ссылке в браузере, чтобы иметь возможность редактировать будущую статью").grid(
            column=0, row=0)
        ttk.Label(accFrm, text="Ссылка: {}".format(account['auth_url'])).grid(column=0, row=1)
        ttk.Button(accFrm, text="Скопировать", command=lambda: copy2clip(account['auth_url'])).grid(column=1, row=1)

    ttk.Button(tokenGenFrm, text="Подтвердить", command=buttonHandler).grid(column=0, row=2)


def chooseDir():
    dirPath = filedialog.askdirectory()
    dirLabel.config(text=dirPath)
    setImgDir(dirPath)


def handleWriteToken(sv):
    setToken(sv.get())


def showError():
    if getToken():
        showwarning(title="Внимание!", message="Не выбран каталог изображений")
    elif getImgDir():
        showwarning(title="Внимание!", message="Вы не указали токен")
    else:
        showwarning(title="Внимание!", message="Вы не указали токен и не выбрали каталог изображений")


def done():
    if getToken() and getImgDir():
        link = createPage()

        localRoot, doneFrm = createWindow()

        ttk.Label(doneFrm, text="Ссылка: {}".format(link)).grid(column=0, row=0)
        ttk.Button(doneFrm, text="Скопировать", command=lambda: copy2clip(link)).grid(column=1, row=0)
    else:
        showError()


root, frm = createWindow()

ttk.Label(frm, text="Токен доступа").grid(column=1, row=0)
ttk.Label(frm, text="Developer hates his life ¯\\_(ツ)_/¯").grid(column=0, row=4)
ttk.Label(frm, text="Made by Lil Dick").grid(column=0, row=5)

sv = StringVar()
sv.trace("w", lambda name, index, mode, sv=sv: handleWriteToken(sv))

tokenInput = ttk.Entry(frm, textvariable=sv)
tokenInput.grid(column=1, row=1)

ttk.Button(frm, text="Создать токен", command=genToken).grid(column=0, row=1)
ttk.Button(frm, text="Загрузить", command=done).grid(column=0, row=2)
ttk.Button(frm, text="Выбрать папку", command=chooseDir).grid(column=0, row=3)

dirLabel = ttk.Label(frm, text="Папка не выбрана")
dirLabel.grid(column=1, row=3)

root.mainloop()
