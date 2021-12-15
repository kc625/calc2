"""Class for the OOP Principles Article Controller"""
from app.controllers.controller import ControllerBase
from flask import render_template

class OOPController(ControllerBase):
    """OOP Principles Article Controller class"""

    @staticmethod
    def get():
        """Get method"""
        return render_template('oop_principles.html')
