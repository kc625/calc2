"""Class for the AAA Testing Article Controller"""
# pylint: disable=no-name-in-module,import-error
from flask import render_template
from app.controllers.controller import ControllerBase

class AAATestingController(ControllerBase):
    """Pylint Article Controller class"""
    # pylint: disable=too-few-public-methods

    @staticmethod
    def get():
        """Get method"""
        return render_template('aaa_testing.html')
