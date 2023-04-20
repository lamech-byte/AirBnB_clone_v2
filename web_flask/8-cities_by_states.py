#!/usr/bin/python3
"""
Starts a Flask web application.
"""
from flask import Flask, render_template
from models import storage
from models.state import State
import os

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_session(exception):
    """Closes the current SQLAlchemy session."""
    storage.close()


@app.route('/cities_by_states')
def display_states_and_cities():
    """Displays a list of all State objects and their cities."""
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        states = storage.all(State).values()
    else:
        states = storage.all("State").values()
    states_sorted = sorted(states, key=lambda state: state.name)
    return render_template('8-cities_by_states.html', states=states_sorted)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
