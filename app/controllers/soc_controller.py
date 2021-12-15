"""Class for the Separation of Concerns Article Controller"""
from app.controllers.controller import ControllerBase
from flask import render_template

class SOCController(ControllerBase):
    """Pylint Article Controller class"""

    @staticmethod
    def get():
        """Get method"""
        return render_template('separation_of_concerns.html')
