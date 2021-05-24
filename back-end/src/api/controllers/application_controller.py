from src.service.application_service import ApplicationService
from src.service.helpers.request_handler import RequestHandler
from src.api.app import app
from flask import request

application_service = ApplicationService()
request_handler = RequestHandler()
api_version = '/api/v1/application'

@app.route(api_version + '/all', methods=['GET'])
def get_applications():
    """
        This is the endpoint returning application list
    """
    api_response = application_service.get_applications()
    return api_response

@app.route(api_version + '/<application_id>', methods=['GET'])
def get_application(application_id):
    """
        This is the endpoint returning a single application with the given id
    """
    api_response = application_service.get_application(application_id)
    return api_response

@app.route(api_version + '/', methods=['POST'])
def insert_application():
    """
        This is the endpoint for creating a new application
    """
    data = request.get_json()
    api_response = application_service.create_application(data)
    return api_response

@app.route(api_version + '/', methods=['DELETE'])
def delete_application():
    """
        This is endpoint for deleting an application 
    """
    data = request.get_json()
    api_response = application_service.delete_application(data)
    return api_response

@app.route(api_version + '/', methods=['PUT'])
def update_application():
    """
        This is endpoint for updating an application 
    """
    data = request.get_json()
    api_response = application_service.update_application(data)
    return api_response


@app.route(api_version + '/status', methods=['PUT'])
def update_application_status():
    """
        This is endpoint for updating the status of the application
    """
    req_handler_response = request_handler.validate_token(request)

    if req_handler_response['success']:
        data = request.get_json()
        api_response = application_service.update_application_status(data)
        return api_response

    return req_handler_response
