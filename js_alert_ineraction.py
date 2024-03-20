from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time


service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service = service)
driver.maximize_window()
driver.implicitly_wait(15)
driver.get("https://www.imdb.com")



# 1 option alert
WebDriverWait(driver, 5).until(expected_conditions.alert_is_present()) # use only if you need
Alert(driver).accept() # accept/OK



# 2 option alert - read alert box
WebDriverWait(driver, 5).until(expected_conditions.alert_is_present()) # use only if you need
message = Alert(driver).text # you can read alert box message
Alert(driver).dismiss() # cancel/give up



# alert box input
WebDriverWait(driver, 5).until(expected_conditions.alert_is_present()) # use only if you need
alert = Alert(driver)
message = alert.text # you can read alert box message
alert.send_keys("test message")
Alert(driver).accept()



