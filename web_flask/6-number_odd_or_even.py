#!/usr/bin/python3
""" Starts a Flash Web Application [ Number template]"""
from flask import Flask, render_template
app = Flask(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

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
    return "python "+ text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def Is_it_a_number(n):
    '''Prints a message when /number is called'''
    return "{:d} is number".format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def Number_template(n):
    '''
    Display n is a number only if n is an integer
    you need to use the method render_templates()
    '''
    return render_template('5-number.html', value=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    """ display a HTML page only if n is an integer """
    return render_template('6-number_odd_or_even.html', value=n)

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)

