#!/usr/bin/python3

""" Flask app """

from flask import Flask, render_template
from models.state import State
from models import storage
app = Flask(__name__)

@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """ states and cities sorted by name """
    states = storage.all("State").values()
    return render_templates("8-cities_by_states.html", states=states)

@app.teardown_appcontext
def teardown(exception):
    """ closing storage teardown """
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
