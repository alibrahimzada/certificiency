# from api import app
from service.event_service import EventService
# from service.user import UserService
# put __init__.py files in each directory
from flask import jsonify, Blueprint, request

event_service = EventService()

bp = Blueprint('event', __name__)
@bp.route('/all', methods=['GET'])
def get_events():
    """
        This is the endpoint returning event list
    """
    events = event_service.get_events()

    return jsonify(events)

@bp.route('/', methods=['POST'])
def insert_event():
    """
        This is the endpoint for creating a new event
    """

    data = request.get_json()
    status = event_service.insert_event(data)
    return status

@bp.route('/', methods=['DELETE'])
def delete_event():
    """
        This is endpoint for deleting an event 
    """
    data = request.get_json()
    status = event_service.delete_event(data)
    return status

@bp.route('/', methods=['PUT'])
def update_event():
    """
        This is endpoint for updating an event 
    """
    data = request.get_json()
    status = event_service.update_event(data)
    return status
