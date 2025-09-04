import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.google.com")
time.sleep(2)

#leiab ja sisestab nime searchi
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Angela Roosmägi") 