"""Calculation history class"""
from calc.calculations.addition import Addition
from calc.calculations.subtraction import Subtraction
from calc.calculations.multiplication import Multiplication
from calc.calculations.division import Division

class Calculations:
    """This class works with the history of the calculator"""

    history = []
    # pylint: disable=too-few-public-methods

    @staticmethod
    def clear_history():
        """Clears all values in history"""
        Calculations.history.clear()
        return True

    @staticmethod
    def count_history():
        """Returns the number of items in the history"""
        return len(Calculations.history)

    @staticmethod
    def get_last_calculation_object():
        """Returns last calculation in history"""
        return Calculations.history[-1]

    @staticmethod
    def get_last_calculation_result():
        """Returns value of last calculation in history"""
        calculation = Calculations.get_last_calculation_object()
        return calculation.get_result()

    @staticmethod
    def get_first_calculation_object():
        """Returns first calculation in history"""
        return Calculations.history[0]

    @staticmethod
    def get_first_calculation_result():
        """Returns value of first calculation in history"""
        calculation = Calculations.get_first_calculation_object()
        return calculation.get_result()

    @staticmethod
    def get_calculation(num):
        """Returns calculation from the given index"""
        return Calculations.history[num]

    @staticmethod
    def add_calculation(calculation):
        """Adds a specific calculation to history"""
        return Calculations.history.append(calculation)

    @staticmethod
    def add_addition_calculation(values):
        """Creates an addition object and adds it to history using factory method create"""
        Calculations.add_calculation(Addition.create(values))
        return True

    @staticmethod
    def add_subtraction_calculation(values):
        """Creates a subtraction object and adds it to history using factory method create"""
        Calculations.add_calculation(Subtraction.create(values))
        return True

    @staticmethod
    def add_multiplication_calculation(values):
        """Creates a multiplication object and adds it to history using factory method create"""
        Calculations.add_calculation(Multiplication.create(values))
        return True

    @staticmethod
    def add_division_calculation(values):
        """Creates a division object and adds it to history using factory method create"""
        Calculations.add_calculation(Division.create(values))
        return True
