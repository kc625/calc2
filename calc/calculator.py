"""This class performs the basic calculator functions"""
from calc.calculations.addition import Addition
from calc.calculations.subtraction import Subtraction
from calc.calculations.multiplication import Multiplication
from calc.calculations.division import Division
from calc.history.calculations import Calculations

class Calculator:
    """ This is my Calculator class"""

    @staticmethod
    def add_numbers(*args):
        """adds list of numbers"""
        addition = Addition(args)
        Calculations.history.append(addition)
        return addition.get_result

    @staticmethod
    def subtract_numbers(*args):
        """subtracts a list of numbers from result"""
        subtraction = Subtraction(args)
        Calculations.history.append(subtraction)
        return subtraction.get_result()

    @staticmethod
    def multiply_numbers(*args):
        """multiplies all numbers together"""
        multiplication = Multiplication(args)
        Calculations.history.append(multiplication)
        return multiplication.get_result()

    @staticmethod
    def divide_numbers(*args):
        """divides each number in the list by the next one, returns an error if any # after the first is 0"""
        division = Division(args)
        Calculations.history.append(division)
        return division.get_result()
