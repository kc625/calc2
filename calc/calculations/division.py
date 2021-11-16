"""This is the Division Class"""
from calc.calculations.calculation import Calculation

class Division(Calculation):
    """Class for the Division calculation"""

    def get_result(self):
        """This does the actual division. Displays an error if dividing by 0"""
        quotient = self.values[0]
        for value in self.values[1:]:
            if value == 0.0:
                return "Error, cannot divide by zero."
            quotient = quotient / value
        return quotient
