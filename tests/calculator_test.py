"""This tests the Calculator class"""
from calculator.main import Calculator

def test_calculator_initial_result():
    """testing that Calculator result is initially 0"""
    calc = Calculator()
    assert calc.result == 0

def test_calculator_get_result():
    """Testing the get_result method of the calculator"""
    calc = Calculator()
    assert calc.get_result() == 0

def test_calculator_add_number():
    """Testing the add method of the calculator"""
    #Arrange by instantiating the Calculator class as calc
    calc = Calculator()
    #Act by calling the method we are testing
    calc.add_number(8)
    #Assert that the results are correct and what we are expecting
    assert calc.result == 8

def test_calculator_subtract():
    """Testing the subtract method of the calculator"""
    calc = Calculator()
    calc.subtract_number(5)
    assert calc.get_result() == -5

def test_calculator_multiply():
    """Testing the multiply method of the calculator"""
    calc = Calculator()
    calc.multiply_numbers(4,5)
    assert calc.get_result() == 20

def test_calculator_divide():
    """Testing the divide method of the calculator"""
    calc = Calculator()
    calc.divide_numbers(18,3)
    assert calc.get_result() == 6

def test_calculator_divide_by_zero():
    """Testing the divide method of the calculator
    when someone attempts to divide by zero"""
    calc = Calculator()
    calc.divide_numbers(4,0)
    assert calc.get_error() == "Error, cannot divide by zero."
