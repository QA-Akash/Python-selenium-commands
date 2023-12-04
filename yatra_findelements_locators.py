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
        alist = driver.find_elements(By.TAG_NAME, "a")
        print(len(alist))  # Basic significance of it is to use it to find the broken links
        for i in alist:
            print(i.text)  # This will print all text associate with anchore tag 'a'
            print("Id is: ", id(i))
        # print(alist)
        time.sleep(4)


findbyid = Test_find_element_id_name()
findbyid.locate_by_linktext()
