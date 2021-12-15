"""Class for the Pylint Article Controller"""
# pylint: disable=no-name-in-module,import-error
from flask import render_template
from app.controllers.controller import ControllerBase

class PylintController(ControllerBase):
    """Pylint Article Controller class"""
    # pylint: disable=too-few-public-methods

    @staticmethod
    def get():
        """Get method"""
        return render_template('pylint_tips.html')
