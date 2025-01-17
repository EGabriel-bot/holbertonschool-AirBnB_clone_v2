#!/usr/bin/python3
""" Starts a Flask web application """
from email.policy import strict
from flask import Flask, render_template
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


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
        Renders an html template
        :param n: the number to render in the template
    """
    if type(n) == int:
        return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    """
        It returns the string "odd" if the number is odd,
        and "even" if the number is even.
        :param n: an integer
    """
    app.jinja_env.trim_blocks = True
    app.jinja_env.lstrip_blocks = True
    if type(n) == int:
        return render_template('6-number_odd_or_even.html', number=n)


if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
