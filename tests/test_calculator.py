"""Unit tests for the Calculator and Calculation classes."""

import pytest
from calculator import Calculator
from calculator.calculation import Calculation

@pytest.mark.parametrize("operation, num1, num2, expected", [
    (Calculator.add, 2, 3, 5),
    (Calculator.subtract, 5, 2, 3),
    (Calculator.multiply, 4, 3, 12),
    (Calculator.divide, 10, 2, 5),
])
def test_operations(operation, num1, num2, expected):
    """Tests basic calculator operations using parameterized testing."""
    assert operation(num1, num2) == expected

def test_divide_by_zero():
    """Tests that division by zero raises a ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        Calculator.divide(5, 0)

def test_calculation():
    """Tests the Calculation class functionality."""
    calc = Calculation(Calculator.add, 2, 3)
    assert calc.result == 5
    assert str(calc) == "2 add 3 = 5"
