from service.role_service import RoleService
from flask import Blueprint, request

role_service = RoleService()

bp = Blueprint('role', __name__)

@bp.route('/all', methods=['GET'])
def get_roles():
    """
        This is the endpoint returning role list
    """
    api_response = role_service.get_roles()
    return api_response

@bp.route('/<role_id>', methods=['GET'])
def get_role(role_id):
    """
        This is the endpoint returning a single role with the given id
    """

    api_response = role_service.get_role(role_id)
    return api_response

@bp.route('/', methods=['POST'])
def insert_role():
    """
        This is the endpoint for creating a new role
    """
    data = request.get_json()
    api_response = role_service.insert_role(data)
    return api_response

@bp.route('/', methods=['DELETE'])
def delete_role():
    """
        This is endpoint for deleting a role 
    """
    data = request.get_json()
    api_response = role_service.delete_role(data)
    return api_response

@bp.route('/', methods=['PUT'])
def update_user():
    """
        This is endpoint for updating a role
    """
    data = request.get_json()
    api_response = role_service.update_role(data)
    return api_response