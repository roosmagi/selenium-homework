import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
time.sleep(2)

#leiab nupu
add_button = driver.find_element(By.XPATH, "//button[text()='Add Element']")

#vajutab nuppu 5 korda
for i in range(5):
    add_button.click()
    time.sleep(0.5)

time.sleep(1)

#leiab delete buttonid
delete_buttons = driver.find_elements(By.XPATH, "//button[text()='Delete']")

#vajutab kõiki delete nuppe
for i, btn in enumerate(delete_buttons, start=1):
    btn.click()
    time.sleep(0.5)

