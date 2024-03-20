from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
import time


service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service = service)
driver.get("https://tr.wikipedia.org/wiki/Anasayfa")
text_box = driver.find_element(By.ID, "mp-tfa")
text = text_box.text.split(':')[0]
print(text)

