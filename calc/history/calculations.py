"""Calculation history class"""
class Calculations:

    history = []
    # pylint: disable=too-few-public-methods

    @staticmethod
    def get_history():
        """Returns the full history object"""
        return Calculations.history

    @staticmethod
    def clear_history():
        """Clears all values in history"""
        Calculations.history.clear()
        return True

    @staticmethod
    def get_last_calculation():
        """Returns last calculation in history"""
        return Calculations.history[-1]

    @staticmethod
    def get_first_calculation():
        """Returns first calculation in history"""
        return Calculations.history[0]

    @staticmethod
    def get_calculation(num):
        """Returns calculation from the given index"""
        return Calculations.history[num]

    @staticmethod
    def add_calculation(calculation):
        """Adds a specific calculation to history"""
        return Calculations.history.append(calculation)

    @staticmethod
    def count_history():
        return len(Calculations.history)