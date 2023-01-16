from telegraph import Telegraph as TelegraphAPI
import requests
import os
from PIL import Image


class Telegraph:
    access_token = None
    imgDir = None

    telegraph = None
    account = None

    _tokenCreated = False

    def __init__(self):
        pass

    def createAccount(self, accName, authorName):
        self.telegraph = TelegraphAPI()
        self.account = self.telegraph.create_account(short_name=accName, author_name=authorName)

        self.access_token = self.account['access_token']
        self._tokenCreated = True

        return self.account

    def setImageDir(self, dir):
        self.imgDir = dir

    def setToken(self, newToken):
        self.access_token = newToken

        self._tokenCreated = newToken != ""

    def isTokenCreated(self):
        return self._tokenCreated

    def isDirChosen(self):
        return bool(self.imgDir)

    def createPage(self):
        if not self.telegraph:
            try:
                self.telegraph = TelegraphAPI(access_token=self.access_token)
                self.telegraph.get_account_info() # check token validity
            except:
                return False

        html_content = ""

        with os.scandir(self.imgDir) as entries:
            for entry in entries:
                fullFileName = '{}/{}'.format(self.imgDir, entry.name)

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

        try:
            response = self.telegraph.create_page(
                'Hey',
                html_content=html_content,
            )
        except:
            return False

        return 'http://telegra.ph/{}'.format(response['path'])


telegraph_instance = Telegraph()
