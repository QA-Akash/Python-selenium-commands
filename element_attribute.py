import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

chrome_binary = "D:/chrome-win64/chrome-win64/chrome.exe"
options = webdriver.ChromeOptions()
options.binary_location = chrome_binary


class Test_getattribute:
    def get_attribute(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        driver.get("https://www.yatra.com")
        attr = driver.find_element(By.ID, "BE_flight_flsearch_btn")
        # print(attr.get_attribute("type"))  # submit
        print(attr.get_attribute("name"))  # search flights


attr_obj = Test_getattribute()
attr_obj.get_attribute()