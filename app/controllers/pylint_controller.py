"""Class for the Pylint Article Controller"""
from app.controllers.controller import ControllerBase
from flask import render_template

class PylintController(ControllerBase):
    """Pylint Article Controller class"""

    @staticmethod
    def get():
        """Get method"""
        return render_template('pylint_tips.html')
