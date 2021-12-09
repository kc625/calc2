"""Class for the Calculator Controller"""
from app.controllers.controller import ControllerBase
from calc.calculator import Calculator
from flask import render_template, request, flash, redirect, url_for

class CalculatorController(ControllerBase):
    """Calculator Controller class"""

    @staticmethod
    def post():
        """Post method"""
        if request.form['value1'] == '' or request.form['value2'] == '':
            error = 'WARNING: You must enter a value for both Value 1 and Value 2'
        else:
            flash('Success! Here are your calculation results:')

            value1 = request.form['value1']
            value2 = request.form['value2']
            operation = request.form['operation']
            my_tuple = (value1, value2)
            getattr(Calculator, operation)(my_tuple)
            result = str(Calculator.get_last_result_value())
            return render_template('result.html', value1 = value1, value2 = value2, operation = operation, result = result)
        return render_template('calculator.html', error = error)

    @staticmethod
    def get():
        """Get method"""
        return render_template('calculator.html')
