""""This is the class for writing a csv file"""
import pandas as pd

class WriteCSV:
    """This class is used to create a log file as a csv"""
    # pylint: disable=too-few-public-methods

    @staticmethod
    def write_csv_file(data_frame, csv_location):
        df = pd.DataFrame(data_frame)
        df.to_csv(csv_location)
        return True
