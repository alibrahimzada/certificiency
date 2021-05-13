from service.application_service import ApplicationService
from flask import Blueprint, request

application_service = ApplicationService()

bp = Blueprint('application', __name__)
@bp.route('/all', methods=['GET'])
def get_applications():
    """
        This is the endpoint returning application list
    """
    api_response = application_service.get_applications()
    return api_response

@bp.route('/', methods=['POST'])
def insert_application():
    """
        This is the endpoint for creating a new application
    """
    data = request.get_json()
    api_response = application_service.create_application(data)
    return api_response

@bp.route('/', methods=['DELETE'])
def delete_application():
    """
        This is endpoint for deleting an application 
    """
    data = request.get_json()
    api_response = application_service.delete_application(data)
    return api_response

@bp.route('/', methods=['PUT'])
def update_application():
    """
        This is endpoint for updating an application 
    """
    data = request.get_json()
    api_response = application_service.update_application(data)
    return api_response
