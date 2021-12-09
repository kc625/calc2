"""Class for the Calculator Controller"""
from app.controllers.controller import ControllerBase
from calc.calculator import Calculator
from flask import render_template, request, flash, redirect, url_for

class CalculatorController(ControllerBase):
    """Calculator Controller class"""

    @staticmethod
    def post():
        if request.form['value1'] == '' or request.form['value2'] == '':
            error = 'You must enter a value for both Value 1 and Value 2'
        else:
            flash('Success! Here is your calculation:')
