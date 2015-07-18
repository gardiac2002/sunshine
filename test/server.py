__author__ = 'sen'

import os

from flask import Flask, make_response

app = Flask(__name__)

@app.route('/')
def index():
    """

    """
    current_dir = os.path.dirname(__file__)
    current_dir_abs = os.path.abspath(current_dir)
    app_path = os.path.join(current_dir_abs, 'index.html')

    assert os.path.exists(app_path), 'Does not exist: %s' % app_path
    return make_response(open(app_path).read())
