#!/usr/bin/python3
""" Starts Flask Web app """

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)

def route_hello():
    """ Displays Hello HBNB """
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
