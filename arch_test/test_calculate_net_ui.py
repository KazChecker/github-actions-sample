from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest

BASE_URL = "http://127.0.0.1:5000"

@pytest.mark.parametrize("brutto, tax_rate, expected", [
    (1230, 23, "1000.0"),  # Przypadek standardowy
    (2160, 8, "2000.0"),   # Niższy VAT
    (0, 23, "0.0"),        # Brak kwoty netto
    (1500, 0, "1500.0"),   # Brak VAT
])

def test_calculate_net_ui(brutto, tax_rate, expected):
    """Test UI for calculating gross from net with various inputs."""
    driver = webdriver.Firefox()  # Initialize WebDriver for Firefox
    driver.get(BASE_URL)  # Open application homepage

    try:
        # Enter data into form
        brutto_field = driver.find_element(By.ID, "brutto")
        brutto_field.send_keys(str(brutto))

        tax_rate_field = driver.find_element(By.ID, "tax_rate_net")
        tax_rate_field.send_keys(str(tax_rate))

        driver.find_element(By.ID, "calculate_net").click()  # Click on button 'Calculate'

        # Wait for the expected result
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.TAG_NAME, "body"), expected)
        )

        # Verify the result
        result = driver.find_element(By.TAG_NAME, "body").text
        assert expected in result, f"Expected {expected}, but got {result}"

    finally:
        driver.quit()  # Ensure browser is closed

