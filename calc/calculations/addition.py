"""This is the Addition Class"""
from calc.calculations.calculation import Calculation

class Addition(Calculation):
    """Class for the Addition calculation"""

    def get_result(self):
        """This does the actual addition."""
        total_sum = 0.0
        for value in self.values:
            total_sum = value + total_sum
        return total_sum
