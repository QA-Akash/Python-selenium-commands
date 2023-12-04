from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

chrome_binary = "D:/chrome-win64/chrome-win64/chrome.exe"
options = webdriver.ChromeOptions()
options.binary_location = chrome_binary
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

driver.get("https://www.yatra.com")

print(driver.title)
depart_from = (By.ID, "BE_flight_origin_city")
going_to = (By.ID, "BE_flight_arrival_city")
date = (By.ID, "//td[@id='28/11/2023']")

driver.find_element(depart_from).send_keys("Aurangabad")
driver.find_element(depart_from).send_keys(Keys.ENTER)
driver.find_element(going_to).send_keys("Delhi")
driver.find_element(going_to).send_keys(Keys.ENTER)

driver.close()
