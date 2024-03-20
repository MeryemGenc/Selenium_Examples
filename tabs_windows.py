from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service = service)
driver.maximize_window()
driver.implicitly_wait(15)
driver.get("https://www.imdb.com")


time.sleep(2)
driver.switch_to.new_window("tab")
driver.get("https://www.google.com")
print(driver.current_window_handle)
google_tab = driver.current_window_handle

time.sleep(2)
driver.switch_to.new_window("window")
driver.get("https://www.youtube.com")
print(driver.current_window_handle)
youtube_tab = driver.current_window_handle
time.sleep(2)


print(driver.window_handles)
driver.switch_to.window(google_tab)
time.sleep(2)
driver.switch_to.window(youtube_tab)
time.sleep(2)
driver.quit()


