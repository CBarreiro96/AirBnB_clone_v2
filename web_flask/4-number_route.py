#!/usr/bin/python3
""" Starts a Flash Web Application [Is it a number?]"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Prints a message when / is called """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Prints a message when /hbnb is called """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """ Prints a message when /c is called """
    return "C " + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def Python_is_cool(text='is_cool'):
    '''Prints a message when /python is called'''
    return "python " + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def Is_it_a_number(n):
    '''Prints a message when /number is called'''
    return "{:d} is number".format(n)

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
