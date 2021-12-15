"""Class for the Separation of Concerns Article Controller"""
# pylint: disable=no-name-in-module,import-error
from flask import render_template
from app.controllers.controller import ControllerBase

class SOCController(ControllerBase):
    """Pylint Article Controller class"""
    # pylint: disable=too-few-public-methods

    @staticmethod
    def get():
        """Get method"""
        return render_template('separation_of_concerns.html')
