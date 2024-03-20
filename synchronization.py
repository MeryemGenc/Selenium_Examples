from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time


service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service = service)
driver.maximize_window()
driver.implicitly_wait(15)
driver.get("https://www.imdb.com")

# for if you need more wait
WebDriverWait(driver, 40).until(expected_conditions.presence_of_element_located(By.XPATH, "a xpath kkclss"))
# fluent wait


# INSTEAD OF TIME.SLEEP()





