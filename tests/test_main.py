"""Unit tests for the command-line calculator."""

import subprocess
import pytest
from calculator import Calculator

@pytest.mark.parametrize("num1, num2, operation, expected_output", [
    ("5", "3", "add", "The result of 5 add 3 is equal to 8"),
    ("10", "2", "subtract", "The result of 10 subtract 2 is equal to 8"),
    ("4", "5", "multiply", "The result of 4 multiply 5 is equal to 20"),
    ("20", "4", "divide", "The result of 20 divide 4 is equal to 5"),
    ("1", "0", "divide", "An error occurred: Cannot divide by zero"),
    ("a", "3", "add", "Invalid number input"),
    ("5", "b", "subtract", "Invalid number input"),
    ("9", "3", "unknown", "Unknown operation"),
])
def test_cli_calculator(num1, num2, operation, expected_output):
    """Test the command-line interface of the calculator."""
    result = subprocess.run(
        ["python3", "main.py", num1, num2, operation],
        capture_output=True,
        text=True,
	check=True
    )

    print(f"\nTest Case: {num1}, {num2}, {operation}")
    print(f"Expected: {repr(expected_output.strip())}")
    print(f"Actual  : {repr(result.stdout.strip())}")

    assert expected_output.strip() == result.stdout.strip()


@pytest.mark.parametrize("num1, num2, operation, expected", [
    (5, 3, "add", 8),
    (10, 2, "subtract", 8),
    (4, 5, "multiply", 20),
    (20, 4, "divide", 5),
    (-5, -3, "add", -8),         # Negative numbers
    (-10, 2, "subtract", -12),   # Subtraction with negatives
    (4.5, 2, "multiply", 9.0),   # Float multiplication
    (5, 2, "divide", 2.5),       # Float division
    (0, 100, "multiply", 0),     # Zero multiplication
])
def test_operations(num1, num2, operation, expected):
    """Test basic calculator operations."""
    assert getattr(Calculator, operation)(num1, num2) == expected

def test_invalid_operation():
    """Test invalid operation handling in CLI."""
    result = subprocess.run(
        ["python3", "main.py", "10", "5", "invalid_op"],
        capture_output=True, text=True, check=True
    )
    assert "Unknown operation" in result.stdout


def test_non_numeric_input():
    """Test handling of non-numeric inputs."""
    result = subprocess.run(
        ["python3", "main.py", "abc", "5", "add"],
        capture_output=True, text=True, check=True
    )
    assert "Invalid number input" in result.stdout

def test_divide_by_zero():
    """Test division by zero raises a ValueError."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        Calculator.divide(5, 0)
