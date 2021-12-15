"""Class for the OOP Principles Article Controller"""
# pylint: disable=no-name-in-module,import-error
from flask import render_template
from app.controllers.controller import ControllerBase

class OOPController(ControllerBase):
    """OOP Principles Article Controller class"""
    # pylint: disable=too-few-public-methods

    @staticmethod
    def get():
        """Get method"""
        return render_template('oop_principles.html')
