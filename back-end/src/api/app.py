from __future__ import absolute_import
from flask import Flask
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
import sys

sys.path.insert(1, os.getcwd() + '/back-end/src')

# put __init__.py files in each directory


app = Flask(__name__)
CORS(app)
# app.config.from_object(os.environ['APP_SETTINGS'])
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
config = {
    "development": "src.config.DevelopmentConfig",
    "testing": "src.config.TestingConfig",
    "production": "src.config.ProductionConfig"
}

# app.config.from_object(config[os.getenv('FLASK_CONFIGURATION', 'development')])

@app.route('/')
def hello():
    return "Hello World!"


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

@app.route('/api/v1/user', methods=['GET'])
def get_users():
    """
        This is the endpoint returning user list
    """
    print("Test")
    return jsonify([{'username': 'ali', 'email': 'ali@gmail.com'}, {'username': 'beyza', 'email': 'beyza@gmail.com'}])

if __name__ == '__main__':
    app.run()