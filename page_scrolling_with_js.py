from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
import time


service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service = service)
driver.maximize_window()
driver.get("https://www.imdb.com")

driver.execute_script("window.scrollBy(0, 300)", "")
time.sleep(3)
# driver.save_screenshot("./yyy.png")

# driver.execute_script("window.scrollBy(0, document.body.scrollHeight)", "") # to end of page

link = driver.find_element(By.PARTIAL_LINK_TEXT, "une") # can be changed.
driver.execute_script("arguments[0].scrollIntoView()", link) # to end of page
driver.execute_script("window.scrollBy(0, -150)", "")




input('')
