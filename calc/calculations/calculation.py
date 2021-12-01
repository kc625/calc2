"""This is our base Calculation class"""
class Calculation:
    """Abstract Base Class used for the other calculations"""
    # pylint: disable=too-few-public-methods

    def __init__(self, values: tuple):
        """Constructor method"""
        self.values = Calculation.convert_args_to_tuple_of_floats(values)

    @classmethod
    def create(cls, values: tuple):
        """Factory method"""
        return cls(values)

    @staticmethod
    def convert_args_to_tuple_of_floats(values):
        """standardizes values to a tuple of floats"""
        list_values_float = []
        for item in values:
            list_values_float.append(float(item))
        return tuple(list_values_float)
