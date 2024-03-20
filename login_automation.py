from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
import time


service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service = service)
driver.get("https://profile.intra.42.fr/")

driver.find_element(By.ID, 'username').send_keys('meri')
driver.find_element(By.ID, 'password').send_keys("meri")
driver.find_element(By.ID, 'kc-login').send_keys(Keys.ENTER)

# url = driver.current_url
# driver.find_element(By.CSS_SELECTOR, "h2 i")
# driver.find_element(By.XPATH, "sfsfd")

# ASSERT usage => over if/else


# should also be tested with invalid username/password

input('')

