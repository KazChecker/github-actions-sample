from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Ustawienia opcji Chrome
options = Options()
options.add_argument("--headless")  # Tryb headless
options.add_argument("--no-sandbox")  # Wymagane w środowiskach CI
options.add_argument("--disable-dev-shm-usage")  # Unikanie problemów z pamięcią

# Lokalizacja ChromeDrivera
service = Service("/usr/bin/chromedriver")

# Inicjalizacja WebDrivera
driver = webdriver.Chrome(service=service, options=options)

# Przykładowy test otwierający stronę Google
driver.get("https://www.google.com")
print("Page title is:", driver.title)

driver.quit()
