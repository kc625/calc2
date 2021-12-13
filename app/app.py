"""A Flask web app"""
from flask import Flask
from app.controllers.index_controller import IndexController
from app.controllers.calculator_controller import CalculatorController
from app.controllers.table_controller import TableController
from werkzeug.debug import DebuggedApplication
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)

@app.route('/', methods=['GET'])
def index_get():
    """Index route response"""
    return IndexController.get()

@app.route('/calculator', methods=['GET'])
def calculator_get():
    """Calculator route response, get function"""
    return CalculatorController.get()

@app.route('/calculator', methods=['POST'])
def calculator_post():
    """Calculator route response, post function"""
    return CalculatorController.post()

@app.route('/calculation_history')
def index():
    """Calculation History route response"""
    return TableController.get()
