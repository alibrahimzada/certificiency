# from api import app
from service.user_service import UserService
# from service.user import UserService
# put __init__.py files in each directory
from flask import jsonify, Blueprint, request

user_service = UserService()

bp = Blueprint('user', __name__)
@bp.route('/get-users', methods=['GET'])
def get_users():
    """
        This is the endpoint returning user list
    """
    users = user_service.get_users()
    return jsonify(users)

@bp.route('/insert-user', methods=['POST'])
def insert_user():
    """
        This is the endpoint for creating a new user
    """

    data = request.get_json()
    status = user_service.insert_user(data)
    return status

@bp.route('/delete-user', methods=['DELETE'])
def delete_user():
    """
        This is endpoint for deleting a user 
    """
    data = request.get_json()
    status = user_service.delete_user(data)
    return status

@bp.route('/update-user', methods=['PUT'])
def update_user():
    """
        This is endpoint for updating a user
    """
    data = request.get_json()
    status = user_service.update_user(data)
    return status
