#!/usr/bin/python3

""" Flask web app """

from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def route_hbnb():
    """ Hello Hbnb"""
    return "Hello HBNB!"

@app.route('/', strict_slashes=False)
def hbnb():
    """" hbnb"""
    return "HBNB"

if __name__ == '__main__':
    app.run(host="0.0.0", port="5000")

