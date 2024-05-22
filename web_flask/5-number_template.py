#!/usr/bin/python3
""" Flask web app """

from flask import Flask, render_template
app = Flask(__name__)



@app.route('/', strict_slashes=False)
def route_hbnb():
    """ Hello Hbnb"""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """" hbnb"""
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """ display c followed by <text> """
    return 'C ' + text.replace('_', ' ')

@app.route('/python', strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def python_is_coll(text= "is cool"):
    """ Python is cool """
    return "Python " + text.replace('_', ' '))

@app.route('/number/<int:n>', strict_slashes=False)
def is_it_number(n):
    """ display n as an int """
    return "%i is a number" %n

@app.route('/number_template/<int:n>', strict_slashes=False)
def template_number(n):
    """ display html page if n is int """
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host="0.0.0", port="5000")
