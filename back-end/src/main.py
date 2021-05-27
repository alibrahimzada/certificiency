from __future__ import absolute_import
import sys
import os

sys.path.insert(1, os.getcwd() + '/back-end')

from src.api.app import app
from flask_cors import CORS

def run_api():
    app.config['CORS_HEADERS'] = 'Content-Type'
    CORS(app)
    app.run(
        host=os.environ.get('HOST', 'localhost'),
        debug=True
        # os.environ.get('DEBUG', True)
    )

run_api()
