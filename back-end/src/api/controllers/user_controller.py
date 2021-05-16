from service.user_service import UserService
from flask import Blueprint, request
from flask_cors import CORS, cross_origin

user_service = UserService()

bp = Blueprint('user', __name__)
CORS(bp)
@bp.route('/all', methods=['GET'])
@cross_origin()
def get_users():
    """
        This is the endpoint returning user list
    """
    api_response = user_service.get_users()
    return api_response

@bp.route('/<user_id>', methods=['GET'])
def get_user(user_id):
    """
        This is the endpoint returning a single user with the given id
    """

    api_response = user_service.get_user(user_id)
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
