""""This is the class for writing a csv file"""
import time
import pandas as pd
from data_utilities.absolute_path import absolutepath
from data_utilities.csv_reader import ReadCSV

class WriteCSV:
    """This class is used to create a log file as a csv"""
    # pylint: disable=line-too-long,consider-using-with

    @staticmethod
    def write_csv_file(data, csv_location):
        """Writes a csv file from the given dataset to the given location"""
        data_frame = pd.DataFrame(data)
        abs_location = absolutepath(csv_location)
        data_frame.to_csv(abs_location)
        return True

    @staticmethod
    def append_csv_file(data, csv_location):
        """Adds data to an existing csv file"""
        data_frame = pd.DataFrame(data)
        abs_location = absolutepath(csv_location)
        data_frame.to_csv(abs_location, mode='a', index=False, header=False)
        return True

    @staticmethod
    def make_log_files(csv):
        """Creates the log files for processing a csv"""
        csv_file_name = csv.split('/')[-1]
        end_location = '/'.join(csv.split('/')[:-2]) + '/logs/'
        standard_log = open(end_location + csv_file_name + '_log.txt', 'w', encoding='utf-8')
        error_log = open(end_location + csv_file_name + '_error_log.txt', 'w', encoding='utf-8')
        operation, history = ReadCSV.find_operation(csv)
        for index,row in enumerate(history):
            if row.get_result() == 'Error: cannot divide by zero.':
                error_log.write(str(index + 1) + ',' + csv_file_name + '\n')
            else:
                standard_log.write(str(time.time()) + ',' + csv_file_name + ',' + str(index + 1) + ',' + operation + str(row.get_result()) + '\n')
        standard_log.close()
        error_log.close()
