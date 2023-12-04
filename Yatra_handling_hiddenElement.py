import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

chrome_binary = "D:/chrome-win64/chrome-win64/chrome.exe"
options = webdriver.ChromeOptions()
options.binary_location = chrome_binary


class Hidden_ele_isDisplayed:
    def demo_hidden_ele(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")
        element = driver.find_element(By.XPATH, '//*[@id="myDIV"]').is_displayed()
        print(element)

        eleDis = driver.find_element(By.XPATH, "//*[@id='main']/button")
        eleDis.click()
        element1 = driver.find_element(By.XPATH, '//*[@id="myDIV"]').is_displayed()
        print(element1)

    def demo_hidden_ele_yatra(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        driver.get("https://www.yatra.com/hotels")
        ele = driver.find_element(By.XPATH, '//*[@id="BE_Hotel_pax_info"]/span/label')
        ele.click()
        time.sleep(3)

        child_add = driver.find_element(By.XPATH, '//*[@id="BE_Hotel_pax_box"]/div[1]/div[2]/div[3]/div/div/span[2]')
        child_add.click()
        time.sleep(4)
        age_display = driver.find_element(By.XPATH,'//*[@id="BE_Hotel_pax_box"]/div[1]/ul/li[2]/div/select')
        print(age_display.is_displayed())

        no_child = driver.find_element(By.XPATH, '//*[@id="BE_Hotel_pax_box"]/div[1]/div[2]/div[3]/div/div/span[1]')
        no_child.click()
        time.sleep(4)
        # age_display1 = driver.find_element(By.XPATH, '//*[@id="BE_Hotel_pax_box"]/div[1]/ul/li[2]/div/select')
        # print(age_display1.is_displayed())


hiddenElem = Hidden_ele_isDisplayed()
hiddenElem.demo_hidden_ele_yatra()

