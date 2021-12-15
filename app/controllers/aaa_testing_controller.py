"""Class for the AAA Testing Article Controller"""
from app.controllers.controller import ControllerBase
from flask import render_template

class AAATestingController(ControllerBase):
    """Pylint Article Controller class"""

    @staticmethod
    def get():
        """Get method"""
        return render_template('aaa_testing.html')
