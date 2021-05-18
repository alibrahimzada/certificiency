from src.service.auth_service import AuthService
from flask import Blueprint, request

auth_service = AuthService()

bp = Blueprint('auth', __name__)

@bp.route('/login', methods=['POST'])
def login():
    """
        This is the endpoint for login procedures
    """
    data = request.get_json()
    print(data)
    api_response = auth_service.login(data)
    return api_response