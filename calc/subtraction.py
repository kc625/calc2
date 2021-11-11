"""This is the subtraction calculation. Values A and B come from the Calculation class"""
from calc.calculation import Calculation

class Subtraction(Calculation):
    """The Subtraction class has one method, to get the result of the calculation.
    A and B come from the Calculation parent Class"""
    def get_result(self):
        """This does the actual subtraction."""
        return self.value_a - self.value_b
