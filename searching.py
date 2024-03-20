from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
import time


# service = Service("chrome_driver_path(good to be in the same path with main.py)-> ./chromedriver.exe -> (.exe: only for windows)")
service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service = service)

driver.get("https://www.duckduckgo.com")
print("URL: " + driver.current_url)
print("TITLE: " + driver.title)
driver.maximize_window()
# driver.get("http://google.com")
# print("URL: " + driver.current_url)
# print("TITLE: " + driver.title)
# driver.back()
# print("URL: " + driver.current_url)
# print("TITLE: " + driver.title)

search_box = driver.find_element(By.ID, "searchbox_input")
search_box.send_keys("Selenium lessons")
search_box.send_keys(Keys.ENTER)
# search_box = driver.find_element(By.ID, "searchbox_button").click()
# input[name='q] -> selector searching for web dev tool -> ?How many of this name are there?? for class => input.classname => this class under that div => "div.classofdiv input.classofinput" -> By.CSS_SELECTOR
input('')















# SCREENSHOT - chrome & driver versions must be compatible 
# wait = WebDriverWait(driver, 10)
# element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
# driver.save_screenshot("./yyy.png")






# driver.forward
# driver.refresh
# driver.close() -> closes the current tab
#driver.quit() # -> closes all the tabs

