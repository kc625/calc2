"""This tests the Calculator class"""
import pytest
from calc.calculator import Calculator
from calc.history.calculations import Calculations

@pytest.fixture
def clear_history_fixture():
    """Clears the history so that each test starts with a blank history"""
    Calculations.clear_history()

def test_calculator_add_static(clear_history_fixture):
    """Testing the static add method of the calculator"""
    # pylint: disable=redefined-outer-name,unused-argument
    my_tuple = (1.0, 3.0, 5.0)
    Calculator.add_numbers(my_tuple)
    assert Calculator.get_last_result_value() == 9.0

def test_calculator_subtract_static(clear_history_fixture):
    """Testing the subtract method of the calculator"""
    # pylint: disable=redefined-outer-name,unused-argument
    my_tuple = (5.0, 2.0, 1.0)
    Calculator.subtract_numbers(my_tuple)
    assert Calculator.get_last_result_value() == 2.0

def test_calculator_multiply(clear_history_fixture):
    """Testing the static multiply method of the calculator"""
    # pylint: disable=redefined-outer-name,unused-argument
    my_tuple = (4.0, 5.0, 2.0)
    Calculator.multiply_numbers(my_tuple)
    assert Calculator.get_last_result_value() == 40.0

def test_calculator_divide(clear_history_fixture):
    """Testing the divide method of the calculator"""
    # pylint: disable=redefined-outer-name,unused-argument
    my_tuple = (18.0, 3.0, 2.0)
    Calculator.divide_numbers(my_tuple)
    assert Calculator.get_last_result_value() == 3.0

def test_calculator_divide_by_zero(clear_history_fixture):
    """Testing the divide method of the calculator if someone attempts to divide by zero"""
    # pylint: disable=redefined-outer-name,unused-argument
    my_tuple = (18.0, 3.0, 0.0)
    Calculator.divide_numbers(my_tuple)
    assert Calculator.get_last_result_value() == "Error, cannot divide by zero."
