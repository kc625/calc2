"""This class performs the basic calculator functions"""
from calc.history.calculations import Calculations

class Calculator:
    """This is my Calculator class"""

    @staticmethod
    def get_last_result_value():
        """This will get the result of the last calculation"""
        return Calculations.get_last_calculation_result()

    @staticmethod
    def addition(tuple_values: tuple):
        """Adds a tuple of numbers together"""
        Calculations.add_addition_calculation(tuple_values)
        return True

    @staticmethod
    def subtraction(tuple_values: tuple):
        """Subtracts a tuple of numbers from the first value"""
        Calculations.add_subtraction_calculation(tuple_values)
        return True

    @staticmethod
    def multiplication(tuple_values: tuple):
        """Multiplies a tuple of numbers together"""
        Calculations.add_multiplication_calculation(tuple_values)
        return True

    @staticmethod
    def division(tuple_values: tuple):
        """Divides number in tuple by the next, returns error if any # after the first is 0"""
        Calculations.add_division_calculation(tuple_values)
        return True
