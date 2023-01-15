from telegraph import Telegraph
import requests
import os
from PIL import Image


access_token = None
imgDir = None

telegraph = None

def createPage():
    global telegraph

    if (not telegraph):
        telegraph = Telegraph(access_token=access_token)

    html_content = ""

    with os.scandir(imgDir) as entries:
        for entry in entries:
            fullFileName = '{}/{}'.format(imgDir, entry.name)

            try:
                with Image.open(fullFileName) as f:
                        width, height = f.size

                        width = width * 0.75
                        height = height * 0.75

                        f.thumbnail({width, height})

                        f.save(fullFileName + ".thumbnail.jpeg", "JPEG")

                        with open(fullFileName + ".thumbnail.jpeg", 'rb') as thumbF:
                            src = requests.post(
                                            'https://telegra.ph/upload', files={'file':
                                                                                ('file', thumbF,
                                                                                'image/jpeg')}).json()[0]['src']

                            html_content = html_content + "<img src='{}' />".format(src)

                        os.remove(fullFileName + ".thumbnail.jpeg")
            except:
                print("{} skipped".format(entry.name))

    response = telegraph.create_page(
        'Hey',
        html_content=html_content,
    )

    return 'http://telegra.ph/{}'.format(response['path'])

def createAccount(accName, authorName):
    global access_token, telegraph

    telegraph = Telegraph()
    account = telegraph.create_account(short_name=accName, author_name=authorName)

    access_token = "Token generated"

    return account

def setToken(tokenValue):
    global access_token
    access_token = tokenValue

def getToken():
    global access_token
    return access_token

def setImgDir(dirPath):
    global imgDir
    imgDir = dirPath

def getImgDir():
    global imgDir
    return imgDir
