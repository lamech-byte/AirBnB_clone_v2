#!/usr/bin/python3
"""
    Script that starts a Flask web application
"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route: /
        Displays: "Hello HBNB!"
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route: /hbnb
        Displays: "HBNB"
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Route: /c/<text>
        Displays: C followed by the value of text (replace '_' with space)
    """
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/', defaults={"text": "is cool"}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """
    Route: /python/(<text>)
        Displays: Python followed by the value of text (replace '_' with space)
    """
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    Route: /number/<n>
        Displays: "<n> is a number" only if n is an integer
    """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Route: /number_template/<n>
        Displays: HTML page only if n is an integer: "Number: n" inside H1 tag
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    Route: /number_odd_or_even/<n>
        Displays: HTML page only if n is an integer: "Number: n is even|odd" inside H1 tag
    """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
