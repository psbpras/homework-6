'''My Calculator Test'''
import pytest
from calculator import add, subtract, multiply, divide

def test_add():
    '''Test that addition function works ''' 
    assert add(2, 3) == 5

def test_subtract():
    '''Test that subtraction function works ''' 
    assert subtract(5, 2) == 3

def test_multiply():
    '''Test that multiplication function works '''  
    assert multiply(4, 3) == 12

def test_divide():
    '''Test that division function works ''' 
    assert divide(10, 2) == 5

def test_divide_by_zero():
    '''Test that divide by zero function works ''' 
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)
