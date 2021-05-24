from src.service.event_service import EventService
from src.service.helpers.request_handler import RequestHandler
from src.api.app import app
from flask import request

event_service = EventService()
request_handler = RequestHandler()
api_version = '/api/v1/event'

@app.route(api_version + '/all', methods=['GET'])
def get_events():
    """
        This is the endpoint returning event list
    """
    api_response = event_service.get_events()
    return api_response

@app.route(api_version + '/<event_id>', methods=['GET'])
def get_event(event_id):
    """
        This is the endpoint returning a single event with the given id
    """
    api_response = event_service.get_event(event_id)
    return api_response

@app.route(api_version + '/', methods=['POST'])
def insert_event():
    """
        This is the endpoint for creating a new event
    """

    data = request.get_json()
    api_response = event_service.insert_event(data)
    return api_response

@app.route(api_version + '/', methods=['DELETE'])
def delete_event():
    """
        This is endpoint for deleting an event 
    """
    data = request.get_json()
    api_response = event_service.delete_event(data)
    return api_response

@app.route(api_version + '/', methods=['PUT'])
def update_event():
    """
        This is endpoint for updating an event 
    """
    data = request.get_json()
    api_response = event_service.update_event(data)
    return api_response

@app.route(api_version + '/my-events', methods=['GET'])
def my_events():
    """
        This is endpoint for fetching all available events for the requested user
    """
    req_handler_response = request_handler.validate_token(request)

    if req_handler_response['success']:
        core_app_context = req_handler_response['core_app_context']
        api_response = event_service.get_my_events(core_app_context)
        return api_response

    return req_handler_response
