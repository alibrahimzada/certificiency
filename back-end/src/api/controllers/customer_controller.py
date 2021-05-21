from src.service.customer_service import CustomerService
from flask import Blueprint, request

customer_service = CustomerService()

bp = Blueprint('customer', __name__)
@bp.route('/all', methods=['GET'])
def get_customers():
    """
        This is the endpoint returning customers list
    """
    api_response = customer_service.get_customers()
    return api_response

@bp.route('/<customer_id>', methods=['GET'])
def get_customer(customer_id):
    """
        This is the endpoint returning a single customer with the given id
    """

    api_response = customer_service.get_customer(customer_id)
    return api_response

@bp.route('/', methods=['POST'])
def insert_customer():
    """
        This is the endpoint for creating a new customer
    """
    data = request.get_json()
    api_response = customer_service.insert_customer(data)
    return api_response

@bp.route('/', methods=['DELETE'])
def delete_customer():
    """
        This is endpoint for deleting a customer
    """
    data = request.get_json()
    api_response = customer_service.delete_customer(data)
    return api_response

@bp.route('/', methods=['PUT'])
def update_customer():
    """
        This is endpoint for updating a customer
    """
    data = request.get_json()
    api_response = customer_service.update_customer(data)
    return api_response

@bp.route('/<customer_id>/make-active', methods=['PUT'])
def make_active(customer_id):
    """
        This is endpoint for updating the is_active attribute
        of the given customer to true
    """
    api_response = customer_service.make_active(customer_id)
    return api_response

@bp.route('/<customer_id>/make-passive', methods=['PUT'])
def make_passive(customer_id):
    """
        This is endpoint for updating the is_active attribute
        of the given customer to false
    """
    api_response = customer_service.make_passive(customer_id)
    return api_response
