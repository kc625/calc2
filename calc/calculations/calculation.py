"""This is our base Calculation class"""
class Calculation:
    """Base Class used for the other calculations"""
    # pylint: disable=too-few-public-methods

    def __init__(self, values: tuple):
        """Constructor method"""
        self.values = Calculation.convert_args_to_list_float(values)


    @staticmethod
    def convert_args_to_list_float(values):
        """standardizes values to a list of floats"""
        list_values_float = []
        for item in values:
            list_values_float.append(float(item))
        return list_values_float
