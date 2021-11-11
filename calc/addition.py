"""This is the addition calculation that inherits the value A and value B from the Calculation class"""
from calc.calculation import Calculation

class Addition(Calculation):
    """The Addition class has one method, to get the result of the calculation.
    A and B come from the Calculation parent Class"""
    def getResult(self):
        return self.value_a + self.value_b