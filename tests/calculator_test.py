"""This tests the Calculator class"""
import pytest
import os
from calc.calculator import Calculator
from calc.history.calculations import Calculations
from data_utilities.csv_reader import ReadCSV
from data_utilities.csv_writer import WriteCSV
from data_utilities.absolute_path import absolutepath

@pytest.fixture
def clear_history_fixture():
    """Clears the history so that each test starts with a blank history"""
    Calculations.clear_history()

def test_calculator_add_csv(clear_history_fixture):
    """Testing the add method of the calculator with a csv"""
    # pylint: disable=redefined-outer-name,unused-argument,not-an-iterable,invalid-sequence-index
    test_csv = absolutepath('tests/test_data/addition_sample.csv')
    test_df = ReadCSV.get_data(test_csv)
    for index in test_df.index:
        test_tuple = (test_df['value_1'][index], test_df['value_2'][index])
        Calculator.add_numbers(test_tuple)
        assert  Calculator.get_last_result_value() == test_df['result'][index]

def test_calculator_subtract_csv(clear_history_fixture):
    """Testing the subtract method of the calculator with a csv"""
    # pylint: disable=redefined-outer-name,unused-argument,not-an-iterable,invalid-sequence-index
    test_csv = absolutepath('tests/test_data/subtraction_sample.csv')
    test_df = ReadCSV.get_data(test_csv)
    for index in test_df.index:
        test_tuple = (test_df['value_1'][index], test_df['value_2'][index])
        Calculator.subtract_numbers(test_tuple)
        assert Calculator.get_last_result_value() == test_df['result'][index]

def test_calculator_multiply_csv(clear_history_fixture):
    """Testing the multiply method of the calculator with a csv"""
    # pylint: disable=redefined-outer-name,unused-argument,not-an-iterable,invalid-sequence-index
    test_csv = absolutepath('tests/test_data/multiplication_sample.csv')
    test_df = ReadCSV.get_data(test_csv)
    for index in test_df.index:
        test_tuple = (test_df['value_1'][index], test_df['value_2'][index])
        Calculator.multiply_numbers(test_tuple)
        assert Calculator.get_last_result_value() == test_df['result'][index]

def test_calculator_divide_csv(clear_history_fixture):
    """Testing the divide method of the calculator with a csv"""
    # pylint: disable=redefined-outer-name,unused-argument,not-an-iterable,invalid-sequence-index
    test_csv = absolutepath('tests/test_data/division_sample.csv')
    test_df = ReadCSV.get_data(test_csv)
    for index in test_df.index:
        test_tuple = (test_df['value_1'][index], test_df['value_2'][index])
        Calculator.divide_numbers(test_tuple)
        assert Calculator.get_last_result_value() == test_df['result'][index]

def test_calculator_divide_by_zero(clear_history_fixture):
    """Testing the divide method of the calculator if someone attempts to divide by zero"""
    # pylint: disable=redefined-outer-name,unused-argument
    my_tuple = (18.0, 3.0, 0.0)
    Calculator.divide_numbers(my_tuple)
    assert Calculator.get_last_result_value() == "Error: cannot divide by zero."

def test_write_csv(clear_history_fixture):
    """Testing the write csv method"""
    # pylint: disable=redefined-outer-name,unused-argument
    test_csv = absolutepath('tests/test_data/addition_sample.csv')
    test_df = ReadCSV.get_data(test_csv)
    file_name = 'csv_output.csv'
    path = 'tests/logs'
    full_path = path + '/' + file_name
    WriteCSV.write_csv_file(test_df, full_path)
    assert os.path.exists(full_path)
