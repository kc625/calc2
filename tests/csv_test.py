"""This tests our csv functions"""
import pytest
import pandas as pd
from data_utilities.csv_reader import ReadCSV

@pytest.fixture
def sample_fixture():
    pass

def test_read_csv(sample_fixture):
    """Testing the output of the read csv class"""
    r = ReadCSV
    df = ReadCSV.get_data("addition_sample.csv")
    sample = df.head()
    assert sample == pd.DataFrame({'value_1': [13, 5, 7, 17, 13], 'value_2': [9, 11, 15, 7, 12], 'result': [22, 16, 22, 24, 25]})