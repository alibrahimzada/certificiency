from __future__ import absolute_import
from flask import Flask
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
# app.config.from_object(os.environ['APP_SETTINGS'])
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)


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
    return jsonify([{'username': 'ali', 'email': 'ali@gmail.com'}])

if __name__ == '__main__':
    app.run()