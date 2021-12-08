""""This is the class for reading a csv file"""
import pandas as pd
from data_utilities.absolute_path import absolutepath
from calc.calculator import Calculator
from calc.history.calculations import Calculations

class ReadCSV:
    """This class is used to read a csv file by the given name"""

    @staticmethod
    def get_data(csv):
        """Reads the the csv and turns it into a dataframe"""
        return pd.read_csv(absolutepath(csv))

    @staticmethod
    def find_operation(csv):
        """Figures out what operation is being used in the csv"""
        Calculations.clear_history()
        csv_data = ReadCSV.get_data(csv).to_numpy()
        if 'add' in csv:
            return ReadCSV.add_file(csv_data)
        if 'subtract' in csv:
            return ReadCSV.subtract_file(csv_data)
        if 'multipl' in csv:
            return ReadCSV.multiply_file(csv_data)
        return ReadCSV.divide_file(csv_data)

    @staticmethod
    def add_file(csv_data):
        """Adds the rows of data"""
        for row in enumerate(csv_data):
            Calculator.addition(tuple(row[1]))
        return 'add', Calculations.history

    @staticmethod
    def subtract_file(csv_data):
        """Subtracts the rows of data"""
        for row in enumerate(csv_data):
            Calculator.subtraction(tuple(row[1]))
        return 'subtract', Calculations.history

    @staticmethod
    def multiply_file(csv_data):
        """Multiplies the rows of data"""
        for row in enumerate(csv_data):
            Calculator.multiplication(tuple(row[1]))
        return 'multiply', Calculations.history

    @staticmethod
    def divide_file(csv_data):
        """Divides the rows of data"""
        for row in enumerate(csv_data):
            Calculator.division(tuple(row[1]))
        return 'divide', Calculations.history
