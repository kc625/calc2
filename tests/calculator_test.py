"""This tests the Calculator class"""
from calculator.main import Calculator

def test_calculator_add():
    """Testing the add method of the calculator"""
    calc = Calculator()
    assert calc.add_numbers(3,5) == 8

def test_calculator_subtract():
    """Testing the subtract method of the calculator"""
    calc = Calculator()
    assert calc.subtract_numbers(0,5) == -5

def test_calculator_multiply():
    """Testing the multiply method of the calculator"""
    calc = Calculator()
    assert calc.multiply_numbers(4,5) == 20

def test_calculator_divide():
    """Testing the divide method of the calculator"""
    calc = Calculator()
    assert calc.divide_numbers(18,3) == 6

def test_calculator_divide_by_zero():
    """Testing the divide method of the calculator if someone attempts to divide by zero"""
    calc = Calculator()
    assert calc.divide_numbers(4,0) == "Error, cannot divide by zero."
