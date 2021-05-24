from src.service.event_category_service import EventCategoryService
from src.api.app import app
from flask import request

event_category_service = EventCategoryService()
api_version = '/api/v1/event_category'

@app.route(api_version + '/all', methods=['GET'])
def get_event_categories():
    """
        This is the endpoint returning event_category list
    """
    api_response = event_category_service.get_event_categories()
    return api_response

@app.route(api_version + '/<event_category_id>', methods=['GET'])
def get_event_category(event_category_id):
    """
        This is the endpoint returning a single event_category with the given id
    """
    api_response = event_category_service.get_event_category(event_category_id)
    return api_response

@app.route(api_version + '/', methods=['POST'])
def insert_event_category():
    """
        This is the endpoint for creating a new event_category
    """
    data = request.get_json()
    api_response = event_category_service.insert_event_category(data)
    return api_response

@app.route(api_version + '/', methods=['DELETE'])
def delete_event_category():
    """
        This is endpoint for deleting a event_category 
    """
    data = request.get_json()
    api_response = event_category_service.delete_event_category(data)
    return api_response

@app.route(api_version + '/', methods=['PUT'])
def update_event_category():
    """
        This is endpoint for updating a event_category
    """
    data = request.get_json()
    api_response = event_category_service.update_event_category(data)
    return api_response
