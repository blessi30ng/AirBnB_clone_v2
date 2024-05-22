#!/usr/bin/python3

""" Flask app """

from flask import Flask, render_template
from models.state import State
from models import storage
app = Flask(__name__)

@app.route('/states_list', strict_slashes=False)
def states_list():
    """ Displays states in alphabetical order"""
    states = storage.all("State")
    sorted_states = sorted(states.values(), key=lambda k: k.name)
    return render_template("7-states_list.html", states=sorted_states)

@app.teardown_appcontext
def teardown(exception):
    """ closing storage teardown """
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
