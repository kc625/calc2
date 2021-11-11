"""This is our calculation base class / Abstract Class"""
class Calculation:

    def __init__(self, value_a, value_b):
        """Constructor"""
        self.value_a = value_a
        self.value_b = value_b

    @classmethod
    def create(cls, value_a, value_b):
        """Class Factory Method, creates the objects"""
        return cls(value_a, value_b)