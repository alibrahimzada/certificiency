from src.service.auth_service import AuthService
from flask import Blueprint, request, jsonify
from src.api.app import app

auth_service = AuthService()

bp = Blueprint('auth', __name__)

from flask_cors import CORS

#CORS(app)

@app.route('/auth/login', methods=['POST'])
def login():
    """
        This is the endpoint for login procedures
    """
    data = request.get_json()
    api_response = auth_service.login(data)
    return api_response
