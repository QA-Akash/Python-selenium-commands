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


class DemoDropdownMultiSelect:
    def sel_easy_multi_dropdown(self):
        # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        driver.get("https://demo.seleniumeasy.com/basic-select-dropdown-demo.html")
        driver.maximize_window()
        multi_dropdown_element = driver.find_element(By.ID, "multi-select")
        dropdownList = Select(multi_dropdown_element)
        dropdownList.select_by_index(0)
        dropdownList.select_by_index(2)
        dropdownList.select_by_index(1)
        dropdownList.select_by_value("Texas")
        dropdownList.select_by_visible_text("Washington")
        time.sleep(4)

        dropdownList.deselect_by_index(2)
        dropdownList.deselect_by_value("Texas")


MultiDropDown = DemoDropdownMultiSelect()
MultiDropDown.sel_easy_multi_dropdown()