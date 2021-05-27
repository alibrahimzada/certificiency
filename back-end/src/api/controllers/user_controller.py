from src.service.user_service import UserService
from src.service.helpers.request_handler import RequestHandler
from src.api.app import app
from flask import request

user_service = UserService()
request_handler = RequestHandler()
api_version = '/api/v1/user'

@app.route('api/v1/user/all', methods=['GET'])
def get_users():
    """
        This is the endpoint returning user list
    """
    req_handler_response = request_handler.validate_token(request)

    if req_handler_response['success']:
        core_app_context = req_handler_response['core_app_context']
        api_response = user_service.get_users(core_app_context)
        return api_response

    return req_handler_response

@app.route(api_version + '/<user_id>', methods=['GET'])
def get_user(user_id):
    """
        This is the endpoint returning a single user with the given id
    """
    req_handler_response = request_handler.validate_token(request)

    if req_handler_response['success']:
        api_response = user_service.get_user(user_id)
        return api_response

    return req_handler_response

@app.route(api_version + '/', methods=['POST'])
def insert_user():
    """
        This is the endpoint for creating a new user
    """
    req_handler_response = request_handler.validate_token(request)

    if req_handler_response['success']:
        core_app_context = req_handler_response['core_app_context']
        data = request.get_json()
        api_response = user_service.insert_user(data)
        return api_response
    
    return req_handler_response

@app.route(api_version + '/', methods=['DELETE'])
def delete_user():
    """
        This is endpoint for deleting a user 
    """
    req_handler_response = request_handler.validate_token(request)

    if req_handler_response['success']:
        core_app_context = req_handler_response['core_app_context']
        data = request.get_json()
        api_response = user_service.delete_user(data)
        return api_response

    return req_handler_response

@app.route(api_version + '/', methods=['PUT'])
def update_user():
    """
        This is endpoint for updating a user
    """
    req_handler_response = request_handler.validate_token(request)

    if req_handler_response['success']:
        core_app_context = req_handler_response['core_app_context']
        data = request.get_json()        
        api_response = user_service.update_user(data)
        return api_response

    return req_handler_response