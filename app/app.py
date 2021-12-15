"""A Flask web app"""
from flask import Flask
from app.controllers.index_controller import IndexController
from app.controllers.calculator_controller import CalculatorController
from app.controllers.table_controller import TableController
from app.controllers.pylint_controller import PylintController
from app.controllers.aaa_testing_controller import AAATestingController
from app.controllers.oop_controller import OOPController
from app.controllers.soc_controller import SOCController
from werkzeug.debug import DebuggedApplication

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

@app.route('/pylint_tips')
def pylint_tips():
    """Pylint Tips route response"""
    return PylintController.get()

@app.route('/aaa_testing')
def aaa_testing():
    """AAA Testing route response"""
    return AAATestingController.get()

@app.route('/oop_principles')
def oop_principles():
    """OOP Principles route response"""
    return OOPController.get()

@app.route('/separation_of_concerns')
def separation_of_concerns():
    """Separation of Concerns route response"""
    return SOCController.get()
