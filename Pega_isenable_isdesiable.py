import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

chrome_binary = "D:/chrome-win64/chrome-win64/chrome.exe"
options = webdriver.ChromeOptions()
options.binary_location = chrome_binary


class Element_iseable_disable():

    def demo_enabled_disabled(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        driver.get("https://training.openspan.com/login")
        demo_state = driver.find_element(By.ID, "login_button").is_enabled()
        print(demo_state)  # False
        demo_user = driver.find_element(By.ID,"user_name")
        demo_pass = driver.find_element(By.ID, "user_pass")
        demo_user.send_keys("asgadfs")
        demo_pass.send_keys("qwerert")
        demo_state = driver.find_element(By.ID, "login_button").is_enabled()
        print(demo_state)  # True



demostate = Element_iseable_disable()
demostate.demo_enabled_disabled()