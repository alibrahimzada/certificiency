from src.service.certificate_service import CertificateService
from src.service.helpers.request_handler import RequestHandler
from src.api.app import app
from flask import request

certificate_service = CertificateService()
request_handler = RequestHandler()
api_version = '/api/v1/certificate'

@app.route(api_version + '/all', methods=['GET'])
def get_certificates():
    """
        This is the endpoint returning certificate list
    """
    req_handler_response = request_handler.validate_token(request)

    if req_handler_response['success']:
        api_response = certificate_service.get_certificates()
        return api_response

    return req_handler_response

@app.route(api_version + '/<certificate_id>', methods=['GET'])
def get_certificate(certificate_id):
    """
        This is the endpoint returning a single certificate with the given id
    """
    req_handler_response = request_handler.validate_token(request)

    if req_handler_response['success']:
        api_response = certificate_service.get_certificate(certificate_id)
        return api_response

    return req_handler_response

@app.route(api_version + '/insert', methods=['POST'])
def insert_certificate():
    """
        This is the endpoint for creating a new certificate
    """
    req_handler_response = request_handler.validate_token(request)

    if req_handler_response['success']:
        data = request.get_json()
        api_response = certificate_service.insert_certificate(data)
        return api_response

    return req_handler_response

@app.route(api_version + '/delete/<certificate_id>', methods=['DELETE'])
def delete_certificate(certificate_id):
    """
        This is endpoint for deleting a certificate 
    """
    req_handler_response = request_handler.validate_token(request)

    if req_handler_response['success']:
        data = request.get_json()
        api_response = certificate_service.delete_certificate(certificate_id)
        return api_response

    return req_handler_response

@app.route(api_version + '/update', methods=['PUT'])
def update_certificate():
    """
        This is endpoint for updating a certificate 
    """
    req_handler_response = request_handler.validate_token(request)

    if req_handler_response['success']:
        data = request.get_json()        
        api_response = certificate_service.update_certificate(data)
        return api_response

    return req_handler_response

@app.route(api_version + '/my-certificates', methods=['GET'])
def get_my_certificates():
    """
        This is endpoint for getting a specific user's certificates 
    """
    req_handler_response = request_handler.validate_token(request)

    if req_handler_response['success']:
        core_app_context = req_handler_response['core_app_context']
        api_response = certificate_service.get_my_certificates(core_app_context)
        return api_response

    return req_handler_response

@app.route(api_version + '/<event_id>/certificates', methods=['GET'])
def get_event_certificates(event_id):
    """
        This is an endpoint for fetching all certificates which belongs to the given
        event id
    """
    req_handler_response = request_handler.validate_token(request)

    if req_handler_response['success']:
        core_app_context = req_handler_response['core_app_context']
        api_response = certificate_service.get_event_certificates(event_id)
        return api_response

    return req_handler_response