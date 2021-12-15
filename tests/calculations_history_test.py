"""Testing the Calculations class and its history"""
import pytest
from calc.history.calculations import Calculations
from calc.calculations.addition import Addition

@pytest.fixture
def clear_history_fixture():
    """Clears the history so that each test starts with a fresh history"""
    Calculations.clear_history()

@pytest.fixture
def setup_addition_calculation_fixture():
    """Adds together two values and enters them into the history to begin each test"""
    values = (1, 2)
    add = Addition(values)
    Calculations.add_calculation(add)

def test_add_calculation_history(clear_history_fixture, setup_addition_calculation_fixture):
    """Tests that the add calculation to history function works"""
    # pylint: disable=redefined-outer-name,unused-argument
    assert Calculations.count_history() == 1
    values = (3, 5)
    add = Addition(values)
    Calculations.add_calculation(add)
    assert Calculations.count_history() == 2

def test_clear_calculations_history(clear_history_fixture, setup_addition_calculation_fixture):
    """Tests that the clear history function works"""
    # pylint: disable=redefined-outer-name,unused-argument
    assert Calculations.count_history() == 1
    Calculations.clear_history()
    assert Calculations.clear_history() is True
    assert Calculations.count_history() == 0

def test_count_history(clear_history_fixture, setup_addition_calculation_fixture):
    """Tests that the count history function works"""
    # pylint: disable=redefined-outer-name,unused-argument
    assert Calculations.count_history() == 1

def test_get_last_calculation_result(clear_history_fixture, setup_addition_calculation_fixture):
    """Tests that the get last calculation result function works"""
    # pylint: disable=redefined-outer-name,unused-argument
    assert Calculations.get_last_calculation_result() == 3

def test_get_first_calculation_result(clear_history_fixture, setup_addition_calculation_fixture):
    """Tests that the get first calculation result function works"""
    # pylint: disable=redefined-outer-name,unused-argument
    assert Calculations.get_first_calculation_result() == 3

def test_get_calculation_result(clear_history_fixture, setup_addition_calculation_fixture):
    """Tests that the get calculation function works"""
    # pylint: disable=redefined-outer-name,unused-argument
    assert Calculations.get_calculation(0).get_result() == 3

def test_get_last_calculation_object(clear_history_fixture, setup_addition_calculation_fixture):
    """Tests that the get last calculation object function works"""
    # pylint: disable=redefined-outer-name,unused-argument
    assert isinstance(Calculations.get_last_calculation_object(), Addition)

def test_get_first_calculation_object(clear_history_fixture, setup_addition_calculation_fixture):
    """Tests that the get first calculation object function works"""
    # pylint: disable=redefined-outer-name,unused-argument
    assert isinstance(Calculations.get_first_calculation_object(), Addition)

def test_calculations_data_methods(clear_history_fixture):
    """Tests that the get data method works, as well as the append data method"""
    # pylint: disable=redefined-outer-name,unused-argument
    test_data = {
        'Value 1': [1],
        'Value 2': [2],
        'Operation': ['addition'],
        'Result': [3]
    }
    Calculations.append_data(1, 2, 'addition', 3)
    assert test_data == Calculations.get_data()
