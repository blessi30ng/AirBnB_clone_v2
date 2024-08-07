#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
	return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
	return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c(text):
	return "C {}".format(text)

@app.route('/python/<text>', strict_slashes=False)
def python(text):
	return "Python {}".format(text)

@app.route('/number/<n>', strict_slsahes=False)
def number(n):
	if n is int:
		return "n is a number"

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
