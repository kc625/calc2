"""Class for the Table Controller"""
# pylint: disable=no-name-in-module,import-error
from flask import render_template
from app.controllers.controller import ControllerBase
from data_utilities.csv_reader import ReadCSV

class TableController(ControllerBase):
    """Table Controller class"""
    # pylint: disable=too-few-public-methods

    @staticmethod
    def get():
        """Get method"""
        data = ReadCSV.get_data('app/controllers/display_data.csv')
        return render_template('calculation_history.html', data=data)
