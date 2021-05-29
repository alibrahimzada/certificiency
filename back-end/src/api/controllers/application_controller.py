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
    req_handler_response = request_handler.validate_token(request)

    if req_handler_response['success']:
        core_app_context = req_handler_response['core_app_context']
        api_response = application_service.get_applications(core_app_context)
        return api_response

    return req_handler_response

@app.route(api_version + '/<application_id>', methods=['GET'])
def get_application(application_id):
    """
        This is the endpoint returning a single application with the given id
    """
    req_handler_response = request_handler.validate_token(request)

    if req_handler_response['success']:
        api_response = application_service.get_application(application_id)
        return api_response

    return req_handler_response    

@app.route(api_version + '/insert', methods=['POST'])
def insert_application():
    """
        This is the endpoint for creating a new application
    """
    req_handler_response = request_handler.validate_token(request)

    if req_handler_response['success']:
        data = request.get_json()
        core_app_context = req_handler_response['core_app_context']
        api_response = application_service.insert_application(data, core_app_context)
        return api_response

    return req_handler_response

@app.route(api_version + '/delete/<application_id>', methods=['DELETE'])
def delete_application(application_id):
    """
        This is endpoint for deleting an application 
    """
    req_handler_response = request_handler.validate_token(request)

    if req_handler_response['success']:
        api_response = application_service.delete_application(application_id)
        return api_response

    return req_handler_response

@app.route(api_version + '/update', methods=['PUT'])
def update_application():
    """
        This is endpoint for updating an application 
    """
    req_handler_response = request_handler.validate_token(request)

    if req_handler_response['success']:
        data = request.get_json()
        api_response = application_service.update_application(data)
        return api_response

    return req_handler_response


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
