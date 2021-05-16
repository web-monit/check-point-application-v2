__author__ = "Manouchehr Rasouli"
__date__ = "23/Aug/2017"

"""
To convert this capture to image use this code

import base64
fh = open("imageToSave.png", "wb+")
fh.write(base64.decodebytes(bytes(result["capture"], "utf-8")))
fh.close()
"""

from selenium import webdriver


class PageScreen:
    def __init__(self, url, result):
        self.driver = webdriver.Chrome()
        self.result = result
        self.url = url

    def do_test(self):
        self.driver.get(self.url["url"])
        self.result["capture"] = self.driver.get_screenshot_as_base64()
        self.driver.quit()
        return self.result
