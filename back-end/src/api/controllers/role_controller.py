from src.service.role_service import RoleService
from src.service.helpers.request_handler import RequestHandler
from src.api.app import app
from flask import request

role_service = RoleService()
request_handler = RequestHandler()
api_version = '/api/v1/role'

# @app.route(api_version + '/all', methods=['GET'])
# def get_roles():
#     """
#         This is the endpoint returning role list
#     """
#     req_handler_response = request_handler.validate_token(request)

#     if req_handler_response['success']:
#         core_app_context = req_handler_response['core_app_context']
#         api_response = role_service.get_roles()
#         return api_response

#     return req_handler_response

# @app.route(api_version + '/<role_id>', methods=['GET'])
# def get_role(role_id):
#     """
#         This is the endpoint returning a single role with the given id
#     """
#     req_handler_response = request_handler.validate_token(request)

#     if req_handler_response['success']:
#         core_app_context = req_handler_response['core_app_context']
#         api_response = role_service.get_role(role_id)
#         return api_response

#     return req_handler_response

# @app.route(api_version + '/', methods=['POST'])
# def insert_role():
#     """
#         This is the endpoint for creating a new role
#     """
#     req_handler_response = request_handler.validate_token(request)

#     if req_handler_response['success']:
#         core_app_context = req_handler_response['core_app_context']
#         data = request.get_json()
#         api_response = role_service.insert_role(data)
#         return api_response

#     return req_handler_response

# @app.route(api_version + '/', methods=['DELETE'])
# def delete_role():
#     """
#         This is endpoint for deleting a role 
#     """
#     req_handler_response = request_handler.validate_token(request)

#     if req_handler_response['success']:
#         core_app_context = req_handler_response['core_app_context']
#         data = request.get_json()
#         api_response = role_service.delete_role(data)
#         return api_response

#     return req_handler_response

# @app.route(api_version + '/', methods=['PUT'])
# def update_user():
#     """
#         This is endpoint for updating a role
#     """
#     req_handler_response = request_handler.validate_token(request)

#     if req_handler_response['success']:
#         core_app_context = req_handler_response['core_app_context']
#         data = request.get_json()
#         api_response = role_service.update_role(data)
#         return api_response

#     return req_handler_response
