import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://quotes.toscrape.com")
time.sleep(2)

#leiab teksti ja autorid
quotes = driver.find_elements(By.CLASS_NAME, "text")
authors = driver.find_elements(By.CLASS_NAME, "author")

#prindib konsoolis teksti koos autoriga
for quote, author in zip(quotes, authors):
    print(f"{quote.text} — {author.text}")

driver.quit()
