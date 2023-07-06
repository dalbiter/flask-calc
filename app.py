# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route("/add")
def add_result():
    """Add a and b parameters."""

    a = int(request.args['a'])
    b = int(request.args['b'])
    result = add(a, b)

    return str(result)

@app.route("/sub")
def sub_result():
    """Subtract a and b parameters."""

    a = int(request.args['a'])
    b = int(request.args['b'])
    result = sub(a, b)

    return str(result)

@app.route("/mult")
def mult_result():
    """Multiply a and b parameters."""

    a = int(request.args['a'])
    b = int(request.args['b'])
    result = mult(a, b)

    return str(result)

@app.route("/div")
def div_result():
    """Divide a and b parameters."""

    a = int(request.args['a'])
    b = int(request.args['b'])
    result = div(a, b)

    return str(result)

