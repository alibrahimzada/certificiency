from src.service.event_service import EventService
from flask import Blueprint, request

event_service = EventService()

bp = Blueprint('event', __name__)
@bp.route('/all', methods=['GET'])
def get_events():
    """
        This is the endpoint returning event list
    """
    api_response = event_service.get_events()
    return api_response

@bp.route('/<event_id>', methods=['GET'])
def get_event(event_id):
    """
        This is the endpoint returning a single event with the given id
    """
    api_response = event_service.get_event(event_id)
    return api_response

@bp.route('/', methods=['POST'])
def insert_event():
    """
        This is the endpoint for creating a new event
    """

    data = request.get_json()
    api_response = event_service.insert_event(data)
    return api_response

@bp.route('/', methods=['DELETE'])
def delete_event():
    """
        This is endpoint for deleting an event 
    """
    data = request.get_json()
    api_response = event_service.delete_event(data)
    return api_response

@bp.route('/', methods=['PUT'])
def update_event():
    """
        This is endpoint for updating an event 
    """
    data = request.get_json()
    api_response = event_service.update_event(data)
    return api_response
