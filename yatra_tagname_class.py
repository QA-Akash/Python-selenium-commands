import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

chrome_binary = "D:/chrome-win64/chrome-win64/chrome.exe"
options = webdriver.ChromeOptions()
options.binary_location = chrome_binary


class Test_find_element_tag:
    def locate_by_tagname(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.maximize_window()
        driver.implicitly_wait(4)
        # driver.find_element(By.TAG_NAME, "input").send_keys("perefalcon619@gmail.com")
        # driver.find_element(By.CLASS_NAME,"yt-sme-mobile-input required_field email-login-box")
        """
            This will through the error becz 'yt-sme-mobile-input required_field email-login-box' 
            this is not the single class it is space seperated classes are ther so for us correct one is
            'email-login-box'
        """
        driver.find_element(By.CLASS_NAME, "email-login-box").send_keys("test@gmail.com")
        time.sleep(4)


findbyid = Test_find_element_tag()
findbyid.locate_by_tagname()
