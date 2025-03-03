"""Unit tests for the calculator module"""

import pytest
from app.calculator import Calculator
from app.command_handler import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

def test_calculator_execute():
    """Tests the calculator execution with an addition command."""
    calc = Calculator()
    command = AddCommand(2, 3)
    result = calc.execute(command)
    assert result == 5

def test_add_command():
    """Tests the AddCommand for correct addition."""
    command = AddCommand(4, 6)
    assert command.execute() == 10

def test_subtract_command():
    """Tests the SubtractCommand for correct subtraction."""
    command = SubtractCommand(10, 4)
    assert command.execute() == 6

def test_multiply_command():
    """Tests the MultiplyCommand for correct multiplication."""
    command = MultiplyCommand(3, 7)
    assert command.execute() == 21

def test_divide_command():
    """Tests the DivideCommand for correct division."""
    command = DivideCommand(10, 2)
    assert command.execute() == 5

def test_divide_by_zero():
    """Tests the DivideCommand to handle division by zero."""
    command = DivideCommand(10, 0)
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        command.execute()
