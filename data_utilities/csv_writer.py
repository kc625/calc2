""""This is the class for writing a csv file"""
import time
import pandas as pd

class WriteCSV:
    """This class is used to create a log file as a csv"""
    # pylint: disable=too-few-public-methods

    @staticmethod
    def make_log_file(data_frame, file, operation, csv):
        """Creates a log file from a dataframe as a csv with given file name and location"""
        log = []
        cols = ['timestamp', 'file', 'record number', 'operation', 'result']
        for index in data_frame.index:
            log.append([time.time(), file, index, operation, data_frame.index['result'][index]])
        df1 = pd.DataFrame(log, columns=cols)
        return df1.to_csv(csv)
