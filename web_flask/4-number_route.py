#!/usr/bin/python3
""" Starts a Flask web application """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """This function prints Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """This function prints HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text=""):
    """This function prints C is fun followed by text passed as a subdomain"""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text="is cool"):
    """This function prints Python is cool followed by
    text passed as a subdomain"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def is_it_a_number(n):
    """
    It checks if the input is a number.
    :param n: the number to be checked
    """
    if type(n) == int:
        return "{} is a number".format(n)


if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
