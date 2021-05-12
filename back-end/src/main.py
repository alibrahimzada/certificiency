from __future__ import absolute_import
import sys
import os
from api.app import app

sys.path.insert(1, os.getcwd() + '/back-end/src')

def run_api():
    app.run(
        host=os.environ.get('HOST', 'localhost'),
        debug=True
        # os.environ.get('DEBUG', True)
    )

run_api()
