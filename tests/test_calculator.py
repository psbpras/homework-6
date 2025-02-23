"""Unit tests for the Calculator module."""

import pytest
from calculator import Calculator
from calculator.calculation import Calculation
from calculator.calculations import Calculations

@pytest.fixture
def setup_test_data():
    """Fixture to set up test calculations and clear history."""
    Calculations.clear_history()  # Ensure a clean history before tests
    test_data = [
        Calculation(Calculator.add, 2, 3),
        Calculation(Calculator.subtract, 5, 2),
        Calculation(Calculator.multiply, 4, 3),
        Calculation(Calculator.divide, 10, 2),
    ]
    for calc in test_data:
        Calculations.add_calculation(calc)
    return test_data

@pytest.mark.parametrize("operation, num1, num2, expected", [
    (Calculator.add, 2, 3, 5),
    (Calculator.subtract, 5, 2, 3),
    (Calculator.multiply, 4, 3, 12),
    (Calculator.divide, 10, 2, 5),
])

def test_operations(operation, num1, num2, expected):
    """Test basic calculator operations."""
    assert operation(num1, num2) == expected

def test_divide_by_zero():
    """Test division by zero raises an error."""
    with pytest.raises(ValueError):
        Calculator.divide(5, 0)

def test_calculation_class():
    """Test Calculation class string representation and result."""
    calc = Calculation(Calculator.add, 2, 3)
    assert calc.result == 5
    assert str(calc) == "2 add 3 = 5"

@pytest.mark.usefixtures("setup_test_data")
def test_calculations_history():
    """Test storing calculations in history."""
    assert len(Calculations.history) == 4

@pytest.mark.usefixtures("setup_test_data")
def test_clear_history():
    """Test clearing the calculations history."""
    Calculations.clear_history()
    assert len(Calculations.history) == 0  # Ensure history is empty after clearing
