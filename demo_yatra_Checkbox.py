import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

chrome_binary = "D:/chrome-win64/chrome-win64/chrome.exe"
options = webdriver.ChromeOptions()
options.binary_location = chrome_binary


class Ele_checkbox:
    def click_checkbox(self):
        # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        driver.get("https://www.yatra.com")
        driver.maximize_window()

        # Click on the icon to open the special offers
        icon = driver.find_element(By.XPATH, '//*[@id="BE_flight_form_wrapper"]/div[3]/div[1]/div[1]/a/i')
        icon.click()
        time.sleep(4)

        # Locate and click the special student offer checkbox
        student_checkbox = driver.find_element(By.XPATH, '//*[@id="special_student_offer"]/a/i')
        student_checkbox.click()

        # Check if the checkbox is selected
        # var1 = student_checkbox.is_selected()
        # print("Special Student Offer Checkbox:", var1)

        # Locate and click the armed forces offer checkbox
        armed_forces_checkbox = driver.find_element(By.XPATH, '//*[@id="armedforces_offer"]/a/i')
        armed_forces_checkbox.click()

        # Check if the checkbox is selected
        check3 = armed_forces_checkbox.is_selected()
        print("Armed Forces Offer Checkbox:", check3)

        time.sleep(4)
        driver.quit()


checkboxObj = Ele_checkbox()
checkboxObj.click_checkbox()

"""class Ele_checkbox:
    def click_checkbox(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        driver.get("https://www.yatra.com")
        driver.maximize_window()
        a = driver.find_element(By.XPATH, '//*[@id="BE_flight_form_wrapper"]/div[3]/div[1]/div[1]/a/i')
        a.click()
        time.sleep(4)
        var1 = driver.find_element(By.XPATH, '//*[@id="BE_flight_form_wrapper"]/div[3]/div[1]/div[1]/a/i').is_selected()
        print(var1)
        driver.find_element(By.XPATH, '//*[@id="special_student_offer"]/a/i').click()
        print(driver.find_element(By.XPATH, '//*[@id="special_student_offer"]/a/i').is_selected())

        check3 = driver.find_element(By.XPATH, '//*[@id="armedforces_offer"]/a/i').is_selected()
        print(check3)
        time.sleep(4)


checkboxObj = Ele_checkbox()
checkboxObj.click_checkbox()"""
