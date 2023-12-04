import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_binary = "D:/chrome-win64/chrome-win64/chrome.exe"
options = webdriver.ChromeOptions()
options.binary_location = chrome_binary

#
"""
Usecase => if you want to verify the text there for web element that matches to expected text in text sheet
"""


class Verify_Page_text:
    def verify_text(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get("https://www.yatra.com")
        Why_book_yt = driver.find_element(By.CLASS_NAME,"whyBookContent").text
        print("Why to book through Yatra:\n\t", Why_book_yt)
        text1 = driver.find_element(By.LINK_TEXT, "Yatra for Business").text
        print(text1)
        time.sleep(4)


verify = Verify_Page_text()
verify.verify_text()

