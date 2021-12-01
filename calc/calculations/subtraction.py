"""This is the Subtraction Class"""
from calc.calculations.calculation import Calculation

class Subtraction(Calculation):
    """Class for the Subtraction calculation"""

    def get_result(self):
        """This does the actual subtraction."""
        difference = self.values[0]
        for value in self.values[1:]:
            difference = difference - value
        return difference
