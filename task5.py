import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("detach", True)  # jätab brauseri avatuks
driver = webdriver.Chrome(options=options)

driver.get("https://the-internet.herokuapp.com/")
time.sleep(2)

#vajutab checkboxes lingile
link = driver.find_element(By.LINK_TEXT, "Checkboxes")
link.click()
time.sleep(2)

#leiab checkboxid
checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")

#Clickib checkboxi
for cb in checkboxes:
    if not cb.is_selected():
        cb.click()

time.sleep(2)

#Läheb tagasi
driver.back()

driver.quit()
