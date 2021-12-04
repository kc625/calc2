""""This is the class for writing a csv file"""
import pandas as pd

class WriteCSV:
    """This class is used to read a csv file by the given name"""
    # pylint: disable=too-few-public-methods

    @staticmethod
    def make_log_file(csv):
        """Returns dataframe of the csv with given file name"""
        return pd.to_csv(csv)
