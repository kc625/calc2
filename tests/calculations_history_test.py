"""Testing the Calculations class and its history"""
import pytest
from calc.history.calculations import Calculations
from calc.calculations.addition import Addition

def test_get_history(clear_history):
    """Testing the get history function"""
    # pylint: disable=redefined-outer-name
    # pylint: disable=unused-argument
    calc = Calculator()
    assert calc.add_numbers(3, 5) == 8
    assert calc.add_numbers(2, 5) == 7
    assert calc.add_numbers(1, 9) == 10
    assert calc.get_history() == Calculator.history

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
