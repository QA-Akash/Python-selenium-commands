import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

chrome_binary = "D:/chrome-win64/chrome-win64/chrome.exe"
options = webdriver.ChromeOptions()
options.binary_location = chrome_binary


class DemoMultiWindow:
    def demo_multi_window(self):
        # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        driver.get("https://www.yatra.com")
        driver.maximize_window()

        # Get the First parent page handle
        parent_handle = driver.current_window_handle
        print(parent_handle)

        # Move to the next window to do this use the command

        # Switch between multiple window 2nd Window
        Visa_new_window = driver.find_element(By.ID, 'booking_engine_visa')
        Visa_new_window.click()

        all_handle = driver.window_handles
        print(len(all_handle))

        print(all_handle)
        for handles in all_handle:
            if handles != parent_handle:
                driver.switch_to.window(handles)
                time.sleep(3)
                # 3rd Window
                Hours_Dubai_Visa = driver.find_element(By.LINK_TEXT, "96 Hours Dubai Visa")
                time.sleep(3)
                driver.execute_script("arguments[0].click();", Hours_Dubai_Visa)
                time.sleep(2)
                driver.close()
                time.sleep(2)
                break
        driver.switch_to.window(parent_handle)
        Visa_new_window = driver.find_element(By.ID, 'booking_engine_visa')
        Visa_new_window.click()
        time.sleep(3)


dMulti = DemoMultiWindow()
dMulti.demo_multi_window()
