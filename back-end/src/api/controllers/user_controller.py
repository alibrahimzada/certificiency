from src.service.user_service import UserService
from src.api.app import app
from flask import request

user_service = UserService()
api_version = '/api/v1/user'

@app.route(api_version + '/all', methods=['GET'])
def get_users():
    """
        This is the endpoint returning user list
    """
    api_response = user_service.get_users()
    return api_response

@app.route(api_version + '/<user_id>', methods=['GET'])
def get_user(user_id):
    """
        This is the endpoint returning a single user with the given id
    """

    api_response = user_service.get_user(user_id)
    return api_response

@app.route(api_version + '/', methods=['POST'])
def insert_user():
    """
        This is the endpoint for creating a new user
    """
    data = request.get_json()
    api_response = user_service.insert_user(data)
    return api_response

@app.route(api_version + '/', methods=['DELETE'])
def delete_user():
    """
        This is endpoint for deleting a user 
    """
    data = request.get_json()
    api_response = user_service.delete_user(data)
    return api_response

@app.route(api_version + '/', methods=['PUT'])
def update_user():
    """
        This is endpoint for updating a user
    """
    data = request.get_json()
    api_response = user_service.update_user(data)
    return api_response
