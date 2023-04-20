#!/usr/bin/python3
""" Starts a Flask web application """

from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ display a HTML page with the list of all State objects present in
        DBStorage sorted by name (A->Z)
    """
    states = sorted(list(storage.all(State).values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """ close the storage """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
