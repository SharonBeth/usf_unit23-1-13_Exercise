# Put your app in here.
"""Calculations based on entry query and output math functions"""

from flask import Flask, request
from operations import add, sub, mult, div
# from operations import sub
# from operations import mult
# from operations import div


app = Flask(__name__)

@app.route('/add/')
def do_add():
    """add a + b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a, b)
    return str(result)

@app.route('/sub/')
def do_sub():
    """sub a - b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a, b)
    return str(result)

@app.route('/mult/')
def do_mult():
    """mult a * b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a, b)
    return str(result)

@app.route('/div/')
def do_div():
    """div a / b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a, b)
    return str(result)

function = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div" : div,
}

@app.route('/math/<func>')
def do_function(func):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = function[func](a, b)
    return str(result)




