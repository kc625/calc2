"""This class performs the basic calculator functions"""
from calc.addition import Addition

class Calculator:
    """ This is my Calculator class"""

    history = []

    @staticmethod
    def add_calculation_to_history(calculation):
        Calculator.history.append(calculation)
        return True

    @staticmethod
    def get_result_of_last_calculation_added_to_history():
        return Calculator.history[-1].getResult()

    @staticmethod
    def history_count():
        return len(Calculator.history)

    @staticmethod
    def add_numbers(value_a, value_b):
        """adds value_a and value_b"""
        addition = Addition.create(value_a, value_b)
        Calculator.add_calculation_to_history(addition)
        return Calculator.get_result_of_last_calculation_added_to_history()

    @staticmethod
    def subtract_numbers(value_a, value_b):
        """subtracts value_b from value_a"""
        return value_a - value_b

    @staticmethod
    def multiply_numbers(value_a, value_b):
        """multiplies value_a by value_b"""
        return value_a * value_b

    @staticmethod
    def divide_numbers(value_a, value_b):
        """divides value_a by value_b, displays an error if value_b is 0"""
        if value_b == 0:
            return "Error, cannot divide by zero."
        return value_a / value_b
