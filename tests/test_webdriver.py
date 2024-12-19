from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.remote.webdriver import WebDriver

# Wskaż lokalizację binarek i ustaw tryb headless
options = Options()
options.binary_location = "/usr/bin/firefox"  # Lokalizacja Firefoksa w Ubuntu
options.add_argument("--headless")  # Tryb headless (bez interfejsu graficznego)

# Lokalizacja Geckodrivera
service = Service("/usr/local/bin/geckodriver", log_path="geckodriver.log")

# Zwiększenie limitu czasu na inicjalizację
WebDriver.W3C_REMOTE_PROTOCOL_TIMEOUT = 300  # Zwiększ limit z 120 do 300 sekund

# Inicjalizacja WebDrivera
driver = webdriver.Firefox(service=service, options=options)

# Przykładowy test otwierający stronę Google
driver.get("https://www.google.com")
print("Page title is:", driver.title)

driver.quit()
