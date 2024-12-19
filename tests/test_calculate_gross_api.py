import pytest
import requests

BASE_URL = "http://127.0.0.1:5000"

@pytest.mark.parametrize("netto, tax_rate, expected_status, expected_value, error_key", [
    (1000, 23, 200, 1230.0, None),  # Standard case
    (2000, 8, 200, 2160.0, None),   # Lower VAT
    (0, 23, 200, 0.0, None),        # Zero net value
    (1500, 0, 200, 1500.0, None),   # Zero VAT
    (1, 100, 200, 2.0, None),       # High VAT rate
    (1000, None, 400, None, "Missing parameters"),  # Missing tax_rate
    (None, 23, 400, None, "Missing parameters"),    # Missing netto
    (-1000, 23, 400, None, "Negative values not allowed"),  # Negative netto
    (1000, -23, 400, None, "Negative values not allowed"),  # Negative tax_rate
    ("abc", 23, 400, None, "Invalid input type"),   # Invalid netto type
])
def test_calculate_gross_api(netto, tax_rate, expected_status, expected_value, error_key):
    """Parameterized tests for calculate_gross API."""
    payload = {}
    if netto is not None:
        payload["netto"] = netto
    if tax_rate is not None:
        payload["tax_rate"] = tax_rate

    response = requests.post(f"{BASE_URL}/calculate_gross", json=payload)
    assert response.status_code == expected_status

    if expected_status == 200:
        assert response.json()["gross"] == pytest.approx(expected_value, rel=1e-9)
    else:
        assert response.json()["error"] == error_key
