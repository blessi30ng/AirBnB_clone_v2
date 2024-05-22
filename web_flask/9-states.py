#!/usr/bin/python3

""" Flask app """

from flask import Flask, render_template
from models.state import State
from models import storage
app = Flask(__name__)

@app.route("/states", strict_slashes=False)
def states():
    """ states by name """
    states = storage.all("State").values()
    return render_template("9-states.html", states=states)

@app.route('/states/<id>' strict_slshes=False)
def states_id(id):
    """ displays info aobout id """
    for state in storage.all("State").values():
        if state.id == id:
            return render_template(9-states.html", states=state)
    return render_template("9-states.html")

@app.teardown_appcontext
def teardown(exception):
    """ closing storage teardown """
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
