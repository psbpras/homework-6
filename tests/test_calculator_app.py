"""Unit tests for the calculator module for dynamic."""

from app.calculator import Calculator
from app.command_handler import AddCommand

def test_calculator_execute():
    """Tests the calculator execution with basic arithmetic."""
    calc = Calculator()
    command = AddCommand(2, 3)
    result = calc.execute(command)
    assert result == 5
