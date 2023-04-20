#!/usr/bin/python3
"""Starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exception):
    """Removes the current SQLAlchemy Session"""
    storage.close()


@app.route('/states')
def states():
    """Displays a HTML page with a list of all State objects"""
    states = storage.all(State).values()
    states = sorted(states, key=lambda x: x.name)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>')
def states_by_id(id):
    """Displays a HTML page with all cities of a State object"""
    state = storage.get(State, id)
    if not state:
        return render_template('9-not_found.html')
    cities = sorted(state.cities, key=lambda x: x.name)
    return render_template('9-states_by_id.html', state=state, cities=cities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
