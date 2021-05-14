from service.user_service import UserService
from flask import Blueprint, request

user_service = UserService()

bp = Blueprint('user', __name__)
@bp.route('/all', methods=['GET'])
def get_users():
    """
        This is the endpoint returning user list
    """
    api_response = user_service.get_users()
    return api_response

@bp.route('/', methods=['POST'])
def insert_user():
    """
        This is the endpoint for creating a new user
    """
    data = request.get_json()
    api_response = user_service.insert_user(data)
    return api_response

@bp.route('/', methods=['DELETE'])
def delete_user():
    """
        This is endpoint for deleting a user 
    """
    data = request.get_json()
    api_response = user_service.delete_user(data)
    return api_response

@bp.route('/', methods=['PUT'])
def update_user():
    """
        This is endpoint for updating a user
    """
    data = request.get_json()
    api_response = user_service.update_user(data)
    return api_response
