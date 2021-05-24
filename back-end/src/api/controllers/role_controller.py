from src.service.role_service import RoleService
from src.api.app import app
from flask import request

role_service = RoleService()
api_version = '/api/v1/role'

@app.route(api_version + '/all', methods=['GET'])
def get_roles():
    """
        This is the endpoint returning role list
    """
    api_response = role_service.get_roles()
    return api_response

@app.route(api_version + '/<role_id>', methods=['GET'])
def get_role(role_id):
    """
        This is the endpoint returning a single role with the given id
    """

    api_response = role_service.get_role(role_id)
    return api_response

@app.route(api_version + '/', methods=['POST'])
def insert_role():
    """
        This is the endpoint for creating a new role
    """
    data = request.get_json()
    api_response = role_service.insert_role(data)
    return api_response

@app.route(api_version + '/', methods=['DELETE'])
def delete_role():
    """
        This is endpoint for deleting a role 
    """
    data = request.get_json()
    api_response = role_service.delete_role(data)
    return api_response

@app.route(api_version + '/', methods=['PUT'])
def update_user():
    """
        This is endpoint for updating a role
    """
    data = request.get_json()
    api_response = role_service.update_role(data)
    return api_response
