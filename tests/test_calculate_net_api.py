import pytest
import requests

BASE_URL = "http://127.0.0.1:5000"

@pytest.mark.parametrize("brutto, tax_rate, expected_status, expected_value, error_key", [
    (1230, 23, 200, 1000.0, None),  # Standard case
    (2160, 8, 200, 2000.0, None),   # Lower VAT
    (0, 23, 200, 0.0, None),        # Zero gross value
    (1500, 0, 200, 1500.0, None),   # Zero VAT
    (1, 100, 200, 0.5, None),       # High VAT rate
    (1230, None, 400, None, "Missing parameters"),  # Missing tax_rate
    (None, 23, 400, None, "Missing parameters"),    # Missing brutto
    (-1230, 23, 400, None, "Negative values not allowed"),  # Negative brutto
    (1230, -23, 400, None, "Negative values not allowed"),  # Negative tax_rate
    ("abc", 23, 400, None, "Invalid input type"),   # Invalid brutto type
])
def test_calculate_net_api(brutto, tax_rate, expected_status, expected_value, error_key):
    """Parameterized tests for calculate_net API."""
    payload = {}
    if brutto is not None:
        payload["brutto"] = brutto
    if tax_rate is not None:
        payload["tax_rate"] = tax_rate

    response = requests.post(f"{BASE_URL}/calculate_net", json=payload)
    assert response.status_code == expected_status

    if expected_status == 200:
        assert response.json()["net"] == pytest.approx(expected_value, rel=1e-9)
    else:
        assert response.json()["error"] == error_key
