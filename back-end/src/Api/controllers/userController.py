# from .api import app
from flask import jsonify

@app.route('/api/v1/user', methods=['GET'])
def get_users():
    """
        This is the endpoint returning user list
    """
    print("Test")
    return jsonify([{'username': 'ali', 'email': 'ali@gmail.com'}])