from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import shutil

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

chromedriver_path = shutil.which("chromedriver")
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.google.com")
assert "Google" in driver.title

driver.quit()
