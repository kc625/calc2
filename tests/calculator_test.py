"""This tests the Calculator class"""
from calculator.main import Calculator

def test_calculator_add():
    """Testing the add method of the calculator"""
    calc = Calculator()
    assert calc.add_numbers(3, 5) == 8
    assert calc.add_numbers(2, 5) == 7
    assert calc.add_numbers(1, 9) == 10
    assert calc.add_numbers(7, 5) == 12
    assert calc.add_numbers(10, 6) == 16
    assert calc.history_count() == 5
    assert calc.get_result_of_last_calculation_added_to_history() == 16

def test_calculator_subtract():
    """Testing the subtract method of the calculator"""
    calc = Calculator()
    assert calc.subtract_numbers(0, 5) == -5

def test_calculator_multiply():
    """Testing the multiply method of the calculator"""
    calc = Calculator()
    assert calc.multiply_numbers(4, 5) == 20

def test_calculator_divide():
    """Testing the divide method of the calculator"""
    calc = Calculator()
    assert calc.divide_numbers(18, 3) == 6

def test_calculator_divide_by_zero():
    """Testing the divide method of the calculator if someone attempts to divide by zero"""
    calc = Calculator()
    assert calc.divide_numbers(4, 0) == "Error, cannot divide by zero."
