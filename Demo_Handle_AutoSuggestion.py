import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

chrome_binary = "D:/chrome-win64/chrome-win64/chrome.exe"
options = webdriver.ChromeOptions()
options.binary_location = chrome_binary

"""
Actual Testing Scenario:- 
Whenever somebody is searching in the auto-suggestion dropdown it should only display 10 values
at time or 20 values at a time autosuggestion

Second thing to verify:
What sort of values you are suggesting so you can get the values out in the list and then verify 
all the values suggested actually contains that keywords o not


"""
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
driver.get("https://www.yatra.com")
driver.maximize_window()


class Handle_Autosuggestion:
    def auto_suggestion_for_departure(self):
        # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        depart_From = driver.find_element(By.XPATH, '//*[@id="BE_flight_origin_city"]')
        depart_From.click()
        time.sleep(2)
        depart_From.send_keys("Mumbai")
        time.sleep(2)
        depart_From.send_keys(Keys.ENTER)
        time.sleep(3)

    def auto_suggestion_going_to(self):
        going_to = driver.find_element(By.ID, 'BE_flight_arrival_city')
        # original xpath = //*[@id="BE_flight_arrival_city"]
        # modified to xpath = //div[1]/li
        # combining this result into all list of suggestions

        # Relative xpath
        #     //div[@class="viewport"]
        # add=> //div[1]/li
        # print(going_to)
        going_to.click()
        going_to.send_keys("New")
        time.sleep(2)
        # going_to.send_keys(Keys.ENTER)
        # time.sleep(3)
        # Used 'find elements' for multiple element
        # Use the for loop to get that all element from elements
        # To get the all auto-suggestion(search) and store it in the element
        search_results = driver.find_elements(By.XPATH, '(//div[@class="viewport"]//div[1]/li)')
        print(len(search_results))

        for results in search_results:
            print(results.text)
            if "New York (JFK)" in results.text:
                time.sleep(2)
                results.click()
                time.sleep(3)
                break

        # print(list(search_result))


autosuggest = Handle_Autosuggestion()
autosuggest.auto_suggestion_for_departure()
autosuggest.auto_suggestion_going_to()
