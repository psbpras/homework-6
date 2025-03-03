"""
Pytest fixtures for testing Calculator operations.
"""

import pytest
from faker import Faker
from calculator import Calculator

fake = Faker()

def pytest_addoption(parser):
    """
    Adds command-line option to specify number of test records.
    """
    parser.addoption("--num_records", action="store", default=10, type=int,
                     help="Number of test records to generate")

@pytest.fixture(scope="session")
def num_records(request):
    """
    Retrieves the number of records specified in the command line.
    """
    return request.config.getoption("--num_records")

@pytest.fixture(scope="module")
def operations():
    """
    Returns a dictionary mapping operation names to Calculator methods.
    """
    return {
        "add": Calculator.add,
        "subtract": Calculator.subtract,
        "multiply": Calculator.multiply,
        "divide": Calculator.divide,
    }

@pytest.fixture(params=[
    (fake.random_int(1, 100), fake.random_int(1, 100), op)
    for op in ["add", "subtract", "multiply", "divide"]
])
def test_data(request):
    """
    Generates random test data for calculator operations.
    """
    return request.param
