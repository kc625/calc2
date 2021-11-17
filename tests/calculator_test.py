"""This tests the Calculator class"""
import pytest
from calc.calculator import Calculator
from calc.history.calculations import Calculations

@pytest.fixture
def clear_history_fixture():
    """Clears the history so that each test starts with a blank history"""
    Calculations.clear_history()

def test_calculator_add(clear_history_fixture):
    """Testing the add method of the calculator"""
    # pylint: disable=redefined-outer-name,unused-argument
    assert Calculator.add_numbers(1.0, 3.0, 5.0) == 9.0

def test_calculator_subtract(clear_history_fixture):
    """Testing the subtract method of the calculator"""
    # pylint: disable=redefined-outer-name,unused-argument
    assert Calculator.subtract_numbers(5.0, 2.0) == 3.0

def test_calculator_multiply(clear_history_fixture):
    """Testing the multiply method of the calculator"""
    # pylint: disable=redefined-outer-name,unused-argument
    assert Calculator.multiply_numbers(4.0, 5.0) == 20

def test_calculator_divide(clear_history_fixture):
    """Testing the divide method of the calculator"""
    # pylint: disable=redefined-outer-name,unused-argument
    assert Calculator.divide_numbers(18.0, 3.0) == 6.0

def test_calculator_divide_by_zero(clear_history_fixture):
    """Testing the divide method of the calculator if someone attempts to divide by zero"""
    # pylint: disable=redefined-outer-name,unused-argument
    assert Calculator.divide_numbers(4.0, 0.0) == "Error, cannot divide by zero."
