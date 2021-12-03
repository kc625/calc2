""""This is the class for reading a csv file"""
import pandas as pd

class ReadCSV:
    """This class is used to read a csv file by the given name"""

    @staticmethod
    def get_data(csv):
        """Returns dataframe of the csv with given file name"""
        return pd.read_csv(csv)
