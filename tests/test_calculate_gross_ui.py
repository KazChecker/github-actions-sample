from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest

BASE_URL = "http://127.0.0.1:5000"

@pytest.mark.parametrize("netto, tax_rate, expected", [
    (1000, 23, "1230.0"),  # Przypadek standardowy
#    (2000, 8, "2160.0"),   # Niższy VAT
#    (0, 23, "0.0"),        # Brak kwoty netto
#    (1500, 0, "1500.0"),   # Brak VAT
])
def test_calculate_gross_ui(netto, tax_rate, expected):
    """Test UI for calculating gross from net with delays for presentation."""
    driver = webdriver.Firefox()  # Initialize WebDriver for Firefox
    driver.get(BASE_URL)  # Open application homepage

    try:
        # Enter data into form with delays for presentation
        netto_field = driver.find_element(By.ID, "netto")
        netto_field.send_keys(str(netto))
        time.sleep(2)  # Allow viewers to see the input step

        tax_rate_field = driver.find_element(By.ID, "tax_rate_gross")
        tax_rate_field.send_keys(str(tax_rate))
        time.sleep(2)  # Allow viewers to see the input step

        calculate_button = driver.find_element(By.ID, "calculate_gross")
        calculate_button.click()  # Click on button 'Calculate'
        time.sleep(2)  # Allow viewers to see the click action

        # Wait for the expected result
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.TAG_NAME, "body"), expected)
        )
        time.sleep(2)  # Allow viewers to see the result

        # Verify the result
        result = driver.find_element(By.TAG_NAME, "body").text
        assert expected in result, f"Expected {expected}, but got {result}"

    finally:
        time.sleep(2)  # Allow viewers to observe browser state before closure
        driver.quit()  # Ensure browser is closed
