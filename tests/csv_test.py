"""This tests the csv writing and log methods"""
import os
import pytest
from calc.history.calculations import Calculations
from data_utilities.csv_reader import ReadCSV
from data_utilities.csv_writer import WriteCSV
from data_utilities.absolute_path import absolutepath

@pytest.fixture
def clear_history_fixture():
    """Clears the history so that each test starts with a blank history"""
    Calculations.clear_history()

def test_write_csv(clear_history_fixture):
    """Testing the write csv method"""
    # pylint: disable=redefined-outer-name,unused-argument
    test_df = ReadCSV.get_data('tests/test_data/addition_sample.csv')
    file_name = 'csv_output.csv'
    path = 'tests/logs'
    full_path = path + '/' + file_name
    WriteCSV.write_csv_file(test_df, full_path)
    assert os.path.exists(full_path)

def test_writing_log_file_addition(clear_history_fixture):
    """Testing the log writing method with addition"""
    # pylint: disable=redefined-outer-name,unused-argument
    WriteCSV.make_log_files('tests/test_data/addition.csv')
    assert os.path.exists(absolutepath('tests/logs/addition.csv_log.txt'))
    assert os.path.exists(absolutepath('tests/logs/addition.csv_error_log.txt'))

def test_writing_log_file_subtraction(clear_history_fixture):
    """Testing the log writing method with subtraction"""
    # pylint: disable=redefined-outer-name,unused-argument
    WriteCSV.make_log_files('tests/test_data/subtraction.csv')
    assert os.path.exists(absolutepath('tests/logs/subtraction.csv_log.txt'))
    assert os.path.exists(absolutepath('tests/logs/subtraction.csv_error_log.txt'))

def test_writing_log_file_multiplication(clear_history_fixture):
    """Testing the log writing method with multiplication"""
    # pylint: disable=redefined-outer-name,unused-argument
    WriteCSV.make_log_files('tests/test_data/multiplication.csv')
    assert os.path.exists(absolutepath('tests/logs/multiplication.csv_log.txt'))
    assert os.path.exists(absolutepath('tests/logs/multiplication.csv_error_log.txt'))

def test_writing_log_file_division(clear_history_fixture):
    """Testing the log writing method with division"""
    # pylint: disable=redefined-outer-name,unused-argument
    WriteCSV.make_log_files('tests/test_data/division.csv')
    assert os.path.exists(absolutepath('tests/logs/division.csv_log.txt'))
    assert os.path.exists(absolutepath('tests/logs/division.csv_error_log.txt'))
