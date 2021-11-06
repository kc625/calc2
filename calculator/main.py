"""This class performs the basic calculator functions"""
class Calculator:
    """ This is my Calculator class"""

    result = 0

    @staticmethod
    def add_numbers(value_a, value_b):
        """adds value_a and value_b"""
        result = value_a + value_b
        return result

    @staticmethod
    def subtract_numbers(value_a, value_b):
        """subtracts value_b from value_a"""
        result = value_a - value_b
        return result

    @staticmethod
    def multiply_numbers(value_a, value_b):
        """multiplies value_a by value_b"""
        result = value_a * value_b
        return result

    @staticmethod
    def divide_numbers(value_a, value_b):
        """divides value_a by value_b, displays an error if value_b is 0"""
        if value_b == 0:
            return "Error, cannot divide by zero."
        result = value_a / value_b
        return result
