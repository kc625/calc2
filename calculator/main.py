""" This is the increment function"""
class Calculator:
    """ This is the Calculator class"""

    result = 0
    error = ""

    def get_result(self):
        """ Get Result of Calculation"""
        return self.result

    def get_error(self):
        """Displays Error Message"""
        return self.error

    def add_number(self, value_a):
        """ adds number to result"""
        self.result = self.result + value_a
        return self.result

    def subtract_number(self, value_a):
        """ subtract number from result"""
        self.result = self.result - value_a
        return self.result

    def multiply_numbers(self, value_a, value_b):
        """multiplies value_a by value_b"""
        self.result = value_a * value_b
        return self.result

    def divide_numbers(self, value_a, value_b):
        """divides value_a by value_b, displays an error if value_b is 0"""
        if value_b == 0:
            self.error = "Error, cannot divide by zero"
            return self.error
        self.result = value_a / value_b
        return self.result
