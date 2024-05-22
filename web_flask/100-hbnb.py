#!/usr/bin/python3

""" Flask app """

from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)


app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Displays main hbnb page """
    states = storage.all("State")
    amenities = storage.all("Amenity")
    places = stoerage.all("Place")
    return render_template("100-hbnb.html",
                           states=states, amenities=amenities, places=places)


@app.teardown_appcontext
def teardown(exception):
    """ closing storage teardown """
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
