from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
import time

# This code written as an example only. Not working. 


service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service = service)
driver.maximize_window()
driver.get("https://www.google.com") 

# RADIO BUTTON & CHECK BOX
element_1 = driver.find_element(By.CSS_SELECTOR, "input[value='Element1']")
print(element_1.is_selected())
element_1.click()
print(element_1.is_selected())



# DROPDOWN
element_2 = driver.find_element(By.ID, "element_2']")
dropdown = Select(element_2)
options = dropdown.options()
for i in options:
    print(i + ' ')
# disaple options is also visible
dropdown.select_by_visible_text("option 1")
time.sleep(3)
dropdown.select_by_index(1) # index is 0 based
time.sleep(3)
dropdown.deselect_by_visible_text("option 1")
time.sleep(3)
dropdown.deselect_by_index(1) # index is 0 based
time.sleep(3)





input('')
