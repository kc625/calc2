"""Class for the Table Controller"""
from app.controllers.controller import ControllerBase
from data_utilities.csv_reader import ReadCSV
from flask import render_template

class TableController(ControllerBase):
    """Table Controller class"""

    @staticmethod
    def get():
        """Get method"""
        data = ReadCSV.get_data('app/controllers/display_data.csv')
        return render_template('calculation_history.html', data=data)
