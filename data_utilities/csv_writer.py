""""This is the class for writing a csv file"""
import pandas as pd
from data_utilities.absolute_path import absolutepath

class WriteCSV:
    """This class is used to create a log file as a csv"""
    # pylint: disable=too-few-public-methods

    @staticmethod
    def write_csv_file(data_frame, csv_location):
        """Writes a csv file from the given dataset to the given location"""
        df = pd.DataFrame(data_frame)
        abs_location = absolutepath(csv_location)
        df.to_csv(abs_location)
        return True
