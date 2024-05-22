#!/usr/bin/python3

""" Flask web app """

from flask import Flask
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

if __name__ == '__main__':
    app.run(host="0.0.0", port="5000")
