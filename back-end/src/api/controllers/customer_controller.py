from service.customer_service import CustomerService
from flask import Blueprint, request

customer_service = CustomerService()

bp = Blueprint('customer', __name__)
@bp.route('/get-customers', methods=['GET'])
def get_customers():
    """
        This is the endpoint returning customers list
    """
    api_response = customer_service.get_customers()
    return api_response

@bp.route('/insert-customer', methods=['POST'])
def insert_customer():
    """
        This is the endpoint for creating a new customer
    """
    data = request.get_json()
    api_response = customer_service.insert_customer(data)
    return api_response

@bp.route('/delete-customer', methods=['DELETE'])
def delete_customer():
    """
        This is endpoint for deleting a customer
    """
    data = request.get_json()
    api_response = customer_service.delete_customer(data)
    return api_response

@bp.route('/update-customer', methods=['PUT'])
def update_customer():
    """
        This is endpoint for updating a customer
    """
    data = request.get_json()
    api_response = customer_service.update_customer(data)
    return api_response
