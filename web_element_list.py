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

driver.find_element(By.ID, "imdbHeader-navDrawerOpen--desktop").click()
time.sleep(5)
driver.find_element(By.XPATH, "//span[text()='Top 250 Movies']").click()
movies = driver.find_elements(By.XPATH, "//table/tbody//tr//td[@class='titleColumn']")

for i in movies:
    if i.text[-5:-1] == "2000":
        print(i.text)

input('')
