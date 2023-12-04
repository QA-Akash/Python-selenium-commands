import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_binary = "D:/chrome-win64/chrome-win64/chrome.exe"
options = webdriver.ChromeOptions()
options.binary_location = chrome_binary


class Verify_Page_text:
    def verify_text(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get("https://www.amazon.in")
        time.sleep(7)
        driver.find_element(By.LINK_TEXT, "All").click()
        time.sleep(4)
        element_text = driver.find_element(By.XPATH, "//*[@id='hmenu-content']/ul[1]/li[21]/div").text
        print(element_text)

        links = driver.find_elements(By.XPATH, '//*[@id="hmenu-content"]/ul[1]/li[position() >= 22 and position() <= '
                                               '25]/a')
        for link in links:
            print(link.text)

        giftCard = driver.find_element(By.LINK_TEXT, "Gift Cards & Mobile Recharges")
        giftCard.click()
        birthday_card = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Birthday Gift Cards"))
        )
        driver.execute_script("arguments[0].click();", birthday_card)
        # birthday_card.click()
        print(driver.title)
        checkbox_brother = driver.find_element(By.CLASS_NAME, 'a-icon-checkbox')
        print(checkbox_brother.is_selected())
        checkbox_brother.click()
        print(driver.title)
        # print(checkbox_brother.is_selected())



text_para = Verify_Page_text()
text_para.verify_text()

        # //*[@id="hmenu-content"]/ul[1]/li[25]/a
        # //*[@id="hmenu-content"]/ul[1]/li[22]/a
        # //*[@id="hmenu-content"]/ul[1]/li[24]/a
        # //*[@id="hmenu-content"]/ul[1]/ul[2]/li[2]/a
        # text1 = driver.find_element(By.LINK_TEXT, "programs & features").text
        # print(text1)
        # aList = driver.find_elements(By.CLASS_NAME, "hmenu-item")
        # print(len(aList))Y

        # for i in aList:
        #     print(i.text)



