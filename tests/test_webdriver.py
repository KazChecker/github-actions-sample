from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

# Wskaż binarkę Firefoksa
options = Options()
options.binary_location = "/usr/bin/firefox"  # Domyślna lokalizacja w Ubuntu
service = Service("/usr/local/bin/geckodriver")  # Lokalizacja geckodriver

# Inicjalizacja WebDrivera z pełną konfiguracją
driver = webdriver.Firefox(service=service, options=options)

# Testowanie (przykład otwarcia strony)
driver.get("https://www.google.com")
print("Page title is:", driver.title)

driver.quit()
