import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../app")))

import pytest

# Importing validate_input function from your main.py file
from main import validate_input

def test_validate_input_valid_float(monkeypatch):
    """Test valid float input."""
    monkeypatch.setattr('builtins.input', lambda _: "123.45")
    assert validate_input("Enter a number: ", float, 0.01) == 123.45

def test_validate_input_invalid_input(monkeypatch):
    """Test invalid input and retry."""
    inputs = iter(["abc", "123.45"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert validate_input("Enter a number: ", float, 0.01) == 123.45

def test_validate_input_below_min_value(monkeypatch):
    """Test input below minimum value."""
    inputs = iter(["-10", "50"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert validate_input("Enter a number: ", float, 0.01) == 50

def test_validate_input_boundary_case(monkeypatch):
    """Test input exactly at the minimum value."""
    monkeypatch.setattr('builtins.input', lambda _: "0.01")
    assert validate_input("Enter a number: ", float, 0.01) == 0.01