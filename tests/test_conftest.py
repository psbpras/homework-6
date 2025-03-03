"""
Tests for pytest fixtures in conftest.py.
"""

import pytest  # Now used explicitly via @pytest.mark

def test_num_records(num_records):
    """Ensure num_records fixture retrieves command-line option correctly"""
    assert isinstance(num_records, int) and num_records > 0

@pytest.mark.usefixtures("operations")
def test_operations(operations):
    """Ensure operations fixture returns correct mapping"""
    assert set(operations.keys()) == {"add", "subtract", "multiply", "divide"}
    assert callable(operations["add"])
    assert callable(operations["divide"])

@pytest.mark.usefixtures("test_data")
def test_test_data(test_data):
    """Ensure test_data fixture generates valid test cases"""
    num1, num2, operation = test_data
    assert isinstance(num1, (int, float))
    assert isinstance(num2, (int, float))
    assert operation in {"add", "subtract", "multiply", "divide"}
