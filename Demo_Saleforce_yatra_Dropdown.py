import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select


chrome_binary = "D:/chrome-win64/chrome-win64/chrome.exe"
options = webdriver.ChromeOptions()
options.binary_location = chrome_binary
# Remember that for the dropdown we have 'select' HTML tag then understand that is the dropdown
# And Followed by the options tags
"""
For this we import the select class selenium.webdriver.support.select
This class will help me to work with dropdown
"""


# There are also the exceptions that it may have <div> tag instead of <select> tag So in this case there might be the
# span and the class and get the value and also have <ul> unordered list within where we get the list of options in
# <li> tag
# For this kind of dropdown this it won't be necessary


class DemoDropdownSingleSelect:
    def saleforce_dropdown(self):
        # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        driver.get("https://www.salesforce.com/in/form/signup/freetrial-sales/?d=topnav2-btn-ft")
        driver.maximize_window()
        dropdwn = driver.find_element(By.NAME, "UserTitle")
        dd = Select(dropdwn)
        dd.select_by_index(1)
        time.sleep(3)

        dd.select_by_value("Developer / Software Engineer")
        time.sleep(3)

        dd.select_by_visible_text("IT Manager")
        time.sleep(3)


dddemo = DemoDropdownSingleSelect()
dddemo.saleforce_dropdown()


