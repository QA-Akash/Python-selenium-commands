import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

chrome_binary = "D:/chrome-win64/chrome-win64/chrome.exe"
options = webdriver.ChromeOptions()
options.binary_location = chrome_binary

class DemoPage:
    def demopage_functionalities(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        driver.get("https://www.yatra.com")
        print(driver.current_url)
        print(driver.title)
        print(driver.current_window_handle)
        driver.maximize_window()
        time.sleep(2)
        driver.fullscreen_window()
        driver.refresh()
        driver.find_element(By.LINK_TEXT, "Villas & Stays").click()
        time.sleep(4)
        driver.back()
        time.sleep(5)
        driver.forward()
        driver.minimize_window()
        time.sleep(3)
        driver.quit()


demo_Page = DemoPage()
demo_Page.demopage_functionalities()
