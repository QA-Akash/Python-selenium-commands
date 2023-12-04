import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

chrome_binary = "D:/chrome-win64/chrome-win64/chrome.exe"
options = webdriver.ChromeOptions()
options.binary_location = chrome_binary


class Test_find_element_id_name():
    def locate_by_id(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element(By.NAME, "login-input").send_keys("perefalcon619@gmail.com")
        time.sleep(4)
        driver.find_element(By.ID, "login-continue-btn").click()
        time.sleep(4)


findbyid = Test_find_element_id_name()
findbyid.locate_by_id()
