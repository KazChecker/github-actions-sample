from selenium import webdriver
from selenium.webdriver.common.by import By

# Inicjalizacja WebDrivera
driver = webdriver.Firefox()

# Otwórz stronę Google
driver.get("https://www.google.com")
print("Page title is:", driver.title)

# Zamknij przeglądarkę
driver.quit()
