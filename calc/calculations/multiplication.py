"""This is the Multiplication Class"""
from calc.calculations.calculation import Calculation

class Multiplication(Calculation):
    """Class for the Multiplication calculation"""

    def get_result(self):
        """This does the actual multiplication."""
        product = 1.0
        for value in self.values:
            product = product * value
        return product
