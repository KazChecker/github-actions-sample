from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

# Wskaż binarkę Firefoksa i dodaj tryb headless
options = Options()
options.binary_location = "/usr/bin/firefox"  # Lokalizacja Firefoksa w Ubuntu
options.add_argument("--headless")  # Tryb headless

service = Service("/usr/local/bin/geckodriver")  # Lokalizacja geckodriver

# Inicjalizacja WebDrivera
driver = webdriver.Firefox(service=service, options=options)

# Testowanie
driver.get("https://www.google.com")
print("Page title is:", driver.title)

driver.quit()
