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
    """Tests that the get last calculation function works"""
    # pylint: disable=redefined-outer-name,unused-argument
    assert Calculations.get_last_calculation().get_result() == 3

def test_get_first_calculation_result(clear_history_fixture, setup_addition_calculation_fixture):
    """Tests that the get first result function works"""
    # pylint: disable=redefined-outer-name,unused-argument
    assert Calculations.get_first_calculation().get_result() == 3

def test_get_calculation_result(clear_history_fixture, setup_addition_calculation_fixture):
    """Tests that the get calculation result function works"""
    # pylint: disable=redefined-outer-name,unused-argument
    assert Calculations.get_calculation(0).get_result() == 3

def test_get_history(clear_history_fixture, setup_addition_calculation_fixture):
    """Testing the get history function"""
    # pylint: disable=redefined-outer-name,unused-argument
    assert Calculations.get_history() == Calculations.history
