import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")
time.sleep(2)

#leiab ja sisestab username
username = driver.find_element(By.ID, "username")
username.send_keys("tomsmith")

#leiab ja sisestab passwordi
password = driver.find_element(By.ID, "password")
password.send_keys("SuperSecretPassword!")

#leiab ja vajutab login
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()
time.sleep(2)

#leiab kas sisselogimine õnnestus või ebaõnnestus
message = driver.find_element(By.ID, "flash").text

if "You logged into a secure area!" in message:
    print("Login õnnestus!")
else:
    print("Login ebaõnnestus!")

