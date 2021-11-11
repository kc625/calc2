"""This tests the Calculator class"""
import pytest

from calculator.main import Calculator

@pytest.fixture
def clear_history():
    """Clears the history so that each test starts with a blank history"""
    Calculator.clear_history()

def test_calculator_add(clear_history):
    """Testing the add method of the calculator"""
    # pylint: disable=redefined-outer-name
    # pylint: disable=unused-argument
    calc = Calculator()
    assert calc.add_numbers(3, 5) == 8
    assert calc.add_numbers(2, 5) == 7
    assert calc.add_numbers(1, 9) == 10
    assert calc.add_numbers(7, 5) == 12
    assert calc.add_numbers(10, 6) == 16
    assert calc.history_count() == 5
    assert calc.get_result_of_last_calculation_added_to_history() == 16

def test_calculator_subtract(clear_history):
    """Testing the subtract method of the calculator"""
    # pylint: disable=redefined-outer-name
    # pylint: disable=unused-argument
    calc = Calculator()
    assert calc.subtract_numbers(0, 5) == -5

def test_calculator_multiply(clear_history):
    """Testing the multiply method of the calculator"""
    # pylint: disable=redefined-outer-name
    # pylint: disable=unused-argument
    calc = Calculator()
    assert calc.multiply_numbers(4, 5) == 20

def test_calculator_divide(clear_history):
    """Testing the divide method of the calculator"""
    # pylint: disable=redefined-outer-name
    # pylint: disable=unused-argument
    calc = Calculator()
    assert calc.divide_numbers(18, 3) == 6

def test_calculator_divide_by_zero(clear_history):
    """Testing the divide method of the calculator if someone attempts to divide by zero"""
    # pylint: disable=redefined-outer-name
    # pylint: disable=unused-argument
    calc = Calculator()
    assert calc.divide_numbers(4, 0) == "Error, cannot divide by zero."

def test_clear_history(clear_history):
    """Tests that the clear history function works"""
    # pylint: disable=redefined-outer-name
    # pylint: disable=unused-argument
    calc = Calculator()
    assert calc.add_numbers(3, 5) == 8
    assert calc.subtract_numbers(0, 5) == -5
    assert calc.multiply_numbers(4, 5) == 20
    assert calc.divide_numbers(18, 3) == 6
    assert calc.clear_history() is True
    assert calc.history_count() == 0

def test_count_history(clear_history):
    """Tests that the count history function works"""
    # pylint: disable=redefined-outer-name
    # pylint: disable=unused-argument
    calc = Calculator()
    assert calc.history_count() == 0
    assert calc.add_numbers(3, 5) == 8
    assert calc.subtract_numbers(0, 5) == -5
    assert calc.history_count() == 2

def test_get_last_calculation_result(clear_history):
    """Tests that the get last result function works"""
    # pylint: disable=redefined-outer-name
    # pylint: disable=unused-argument
    calc = Calculator()
    assert calc.add_numbers(3, 5) == 8
    assert calc.multiply_numbers(4, 5) == 20
    assert calc.get_result_of_last_calculation_added_to_history() == 20

def test_get_first_calculation_result(clear_history):
    """Tests that the get first result function works"""
    # pylint: disable=redefined-outer-name
    # pylint: disable=unused-argument
    calc = Calculator()
    assert calc.add_numbers(3, 5) == 8
    assert calc.multiply_numbers(4, 5) == 20
    assert calc.get_result_of_first_calculation_added_to_history() == 8
