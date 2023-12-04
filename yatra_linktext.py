import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

chrome_binary = "D:/chrome-win64/chrome-win64/chrome.exe"
options = webdriver.ChromeOptions()
options.binary_location = chrome_binary


class Test_find_element_id_name:
    def locate_by_linktext(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        driver.get("https://www.yatra.com")
        driver.maximize_window()
        driver.implicitly_wait(4)
        # driver.find_element(By.LINK_TEXT, "Yatra for Business").click()
        # driver.find_element(By.PARTIAL_LINK_TEXT, "Yatra for").click()
        driver.find_element(By.PARTIAL_LINK_TEXT, "Holid").click()
        time.sleep(4)


findbyid = Test_find_element_id_name()
findbyid.locate_by_linktext()
