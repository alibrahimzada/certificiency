# from api import app
from service.event_service import EventService
# from service.user import UserService
# put __init__.py files in each directory
from flask import jsonify, Blueprint, request

event_service = EventService()

bp = Blueprint('event', __name__)
@bp.route('/get-events', methods=['GET'])
def get_events():
    """
        This is the endpoint returning event list
    """
    events = event_service.get_events()

    return jsonify(events)

@bp.route('/create-event', methods=['POST'])
def create_event():
    """
        This is the endpoint for creating a new event
    """

    data = request.get_json()
    event_service.create_event(data)

    return 'worked'


@bp.route('/delete-event', methods=['DELETE'])
def delete_event():
    """
        This is endpoint for deleting a new event 
    """
    data = request.get_json()
    event_service.delete_event(data)
    print(data)
    return "deleted"


@bp.route('/update-event', methods=['PUT'])
def update_event():
    """
        This is endpoint for updating a new event 
    """
    data = request.get_json()
    event_service.update_event(data)
    return "updated"