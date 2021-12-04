""""This is the class for reading a csv file"""
import pandas as pd

class ReadCSV:
    """This class is used to read a csv file by the given name"""
    # pylint: disable=too-few-public-methods
    df = []

    @staticmethod
    def get_data(csv):
        """Reads the the csv and turns it into a dataframe"""
        ReadCSV.df = pd.read_csv(csv)
        return ReadCSV.df
