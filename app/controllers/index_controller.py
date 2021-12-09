"""Class for the Index Controller"""
from app.controllers.controller import ControllerBase
from flask import render_template

class IndexController(ControllerBase):
    """Index Controller class"""

    @staticmethod
    def get():
        """Get method"""
        return render_template('index.html')
