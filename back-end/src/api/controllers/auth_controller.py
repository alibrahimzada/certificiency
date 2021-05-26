from src.service.auth_service import AuthService
from src.api.app import app
from flask import request

auth_service = AuthService()
# api_version = '/api/v1/auth'

@app.route('/api/v1/auth/login', methods=['POST'])
def login():
    """
        This is the endpoint for login procedures
    """
    data = request.get_json()
    api_response = auth_service.login(data)
    return api_response
