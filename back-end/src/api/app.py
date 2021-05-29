from __future__ import absolute_import
from flask import Flask, request
from src.service.auth_service import AuthService
from src.service.user_service import UserService
from src.service.role_service import RoleService
from src.service.customer_service import CustomerService
from src.service.event_category_service import EventCategoryService
from src.service.event_service import EventService
from src.service.application_service import ApplicationService
from src.service.certificate_service import CertificateService
from src.service.helpers.request_handler import RequestHandler
from flask_cors import cross_origin

# put __init__.py files in each directory

app = Flask(__name__)
#CORS(app, origins='*')
# CORS(app)
# app.config.from_object(os.environ['APP_SETTINGS'])
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
config = {
    "development": "src.config.DevelopmentConfig",
    "testing": "src.config.TestingConfig",
    "production": "src.config.ProductionConfig"
}

auth_service = AuthService()
user_service = UserService()
role_service = RoleService()
customer_service = CustomerService()
event_category_service = EventCategoryService()
event_service = EventService()
application_service = ApplicationService()
certificate_service = CertificateService()
request_handler = RequestHandler()
# app.config.from_object(config[os.getenv('FLASK_CONFIGURATION', 'development')])

@app.route('/')
def hello():
    return {"test": "Hello World!"}

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

@app.route('/api/v1/auth/login', methods=['POST'])
def login():
    """
        This is the endpoint for login procedures
    """
    data = request.get_json()
    api_response = auth_service.login(data)
    return api_response

@app.route('/api/v1/user/all', methods=['GET'])
def get_users():
    """
        This is the endpoint returning user list
    """
    req_handler_response = request_handler.validate_token(request)

    if req_handler_response['success']:
        core_app_context = req_handler_response['core_app_context']
        api_response = user_service.get_users(core_app_context)
        return api_response

    return req_handler_response

@app.route('/api/v1/user/<user_id>', methods=['GET'])
def get_user(user_id):
    """
        This is the endpoint returning a single user with the given id
    """
    req_handler_response = request_handler.validate_token(request)

    if req_handler_response['success']:
        core_app_context = req_handler_response['core_app_context']
        api_response = user_service.get_user(user_id)
        return api_response

    return req_handler_response

@app.route('/api/v1/user/insert', methods=['POST'])
def insert_user():
    """
        This is the endpoint for creating a new user
    """
    req_handler_response = request_handler.validate_token(request)

    if req_handler_response['success']:
        core_app_context = req_handler_response['core_app_context']
        data = request.get_json()
        api_response = user_service.insert_user(data, core_app_context)
        return api_response

    return req_handler_response

@app.route('/api/v1/user/delete/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    """
        This is endpoint for deleting a user 
    """
    req_handler_response = request_handler.validate_token(request)

    if req_handler_response['success']:
        core_app_context = req_handler_response['core_app_context']
        api_response = user_service.delete_user(user_id)
        return api_response

    return req_handler_response

@app.route('/api/v1/user/update', methods=['PUT'])
def update_user():
    """
        This is endpoint for updating a user
    """
    req_handler_response = request_handler.validate_token(request)

    if req_handler_response['success']:
        core_app_context = req_handler_response['core_app_context']
        data = request.get_json()
        api_response = user_service.update_user(data)
        return api_response

    return req_handler_response

@app.route('/api/v1/role/all', methods=['GET'])
def get_roles():
    """
        This is the endpoint returning role list
    """
    req_handler_response = request_handler.validate_token(request)

    if req_handler_response['success']:
        core_app_context = req_handler_response['core_app_context']
        api_response = role_service.get_roles(core_app_context)
        return api_response

    return req_handler_response

@app.route('/api/v1/role/<role_id>', methods=['GET'])
def get_role(role_id):
    """
        This is the endpoint returning a single role with the given id
    """
    req_handler_response = request_handler.validate_token(request)

    if req_handler_response['success']:
        core_app_context = req_handler_response['core_app_context']
        api_response = role_service.get_role(role_id)
        return api_response

    return req_handler_response

@app.route('/api/v1/role/insert', methods=['POST'])
def insert_role():
    """
        This is the endpoint for creating a new role
    """
    req_handler_response = request_handler.validate_token(request)

    if req_handler_response['success']:
        core_app_context = req_handler_response['core_app_context']
        data = request.get_json()
        api_response = role_service.insert_role(data, core_app_context)
        return api_response

    return req_handler_response

@app.route('/api/v1/role/delete/<role_id>', methods=['DELETE'])
def delete_role(role_id):
    """
        This is endpoint for deleting a role 
    """
    req_handler_response = request_handler.validate_token(request)

    if req_handler_response['success']:
        core_app_context = req_handler_response['core_app_context']
        api_response = role_service.delete_role(role_id)
        return api_response

    return req_handler_response

@app.route('/api/v1/role/update', methods=['PUT'])
def update_role():
    """
        This is endpoint for updating a role
    """
    req_handler_response = request_handler.validate_token(request)

    if req_handler_response['success']:
        core_app_context = req_handler_response['core_app_context']
        data = request.get_json()
        api_response = role_service.update_role(data, core_app_context)
        return api_response

    return req_handler_response

@app.route('/api/v1/customer/all', methods=['GET'])
def get_customers():
    """
        This is the endpoint returning customers list
    """
    req_handler_response = request_handler.validate_token(request)

    if req_handler_response['success']:
        core_app_context = req_handler_response['core_app_context']
        api_response = customer_service.get_customers()
        return api_response

    return req_handler_response

@app.route('/api/v1/customer/<customer_id>', methods=['GET'])
def get_customer(customer_id):
    """
        This is the endpoint returning a single customer with the given id
    """
    req_handler_response = request_handler.validate_token(request)

    if req_handler_response['success']:
        core_app_context = req_handler_response['core_app_context']
        api_response = customer_service.get_customer(customer_id)
        return api_response

    return req_handler_response

@app.route('/api/v1/customer/insert', methods=['POST'])
def insert_customer():
    """
        This is the endpoint for creating a new customer
    """
    req_handler_response = request_handler.validate_token(request)

    if req_handler_response['success']:
        core_app_context = req_handler_response['core_app_context']
        data = request.get_json()
        api_response = customer_service.insert_customer(data)
        return api_response

    return req_handler_response

@app.route('/api/v1/customer/delete/<customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    """
        This is endpoint for deleting a customer
    """
    req_handler_response = request_handler.validate_token(request)

    if req_handler_response['success']:
        core_app_context = req_handler_response['core_app_context']
        api_response = customer_service.delete_customer(customer_id)
        return api_response

    return req_handler_response

@app.route('/api/v1/customer/update', methods=['PUT'])
def update_customer():
    """
        This is endpoint for updating a customer
    """
    req_handler_response = request_handler.validate_token(request)

    if req_handler_response['success']:
        core_app_context = req_handler_response['core_app_context']
        data = request.get_json()
        api_response = customer_service.update_customer(data)
        return api_response

    return req_handler_response

@app.route('/api/v1/customer/<customer_id>/make-active', methods=['PUT'])
def make_active(customer_id):
    """
        This is endpoint for updating the is_active attribute
        of the given customer to true
    """
    req_handler_response = request_handler.validate_token(request)

    if req_handler_response['success']:
        core_app_context = req_handler_response['core_app_context']
        api_response = customer_service.make_active(customer_id)
        return api_response

    return req_handler_response

@app.route('/api/v1/customer/<customer_id>/make-passive', methods=['PUT'])
def make_passive(customer_id):
    """
        This is endpoint for updating the is_active attribute
        of the given customer to false
    """
    req_handler_response = request_handler.validate_token(request)

    if req_handler_response['success']:
        core_app_context = req_handler_response['core_app_context']
        api_response = customer_service.make_passive(customer_id)
        return api_response

    return req_handler_response

@app.route('/api/v1/event_category/all', methods=['GET'])
def get_event_categories():
    """
        This is the endpoint returning event_category list
    """
    req_handler_response = request_handler.validate_token(request)

    if req_handler_response['success']:
        core_app_context = req_handler_response['core_app_context']
        api_response = event_category_service.get_event_categories()
        return api_response

    return req_handler_response

@app.route('/api/v1/event_category/<event_category_id>', methods=['GET'])
def get_event_category(event_category_id):
    """
        This is the endpoint returning a single event_category with the given id
    """
    req_handler_response = request_handler.validate_token(request)

    if req_handler_response['success']:
        core_app_context = req_handler_response['core_app_context']
        api_response = event_category_service.get_event_category(event_category_id)
        return api_response

    return req_handler_response

@app.route('/api/v1/event_category/insert', methods=['POST'])
def insert_event_category():
    """
        This is the endpoint for creating a new event_category
    """
    req_handler_response = request_handler.validate_token(request)

    if req_handler_response['success']:
        core_app_context = req_handler_response['core_app_context']
        data = request.get_json()
        api_response = event_category_service.insert_event_category(data)
        return api_response

    return req_handler_response

@app.route('/api/v1/event_category/delete/<event_category_id>', methods=['DELETE'])
def delete_event_category(event_category_id):
    """
        This is endpoint for deleting a event_category 
    """
    req_handler_response = request_handler.validate_token(request)

    if req_handler_response['success']:
        core_app_context = req_handler_response['core_app_context']
        api_response = event_category_service.delete_event_category(event_category_id)
        return api_response

    return req_handler_response

@app.route('/api/v1/event_category/update', methods=['PUT'])
def update_event_category():
    """
        This is endpoint for updating a event_category
    """
    req_handler_response = request_handler.validate_token(request)

    if req_handler_response['success']:
        core_app_context = req_handler_response['core_app_context']
        data = request.get_json()
        api_response = event_category_service.update_event_category(data)
        return api_response

    return req_handler_response

@app.route('/api/v1/event/all', methods=['GET'])
def get_events():
    """
        This is the endpoint returning event list
    """
    req_handler_response = request_handler.validate_token(request)

    if req_handler_response['success']:
        core_app_context = req_handler_response['core_app_context']
        api_response = event_service.get_events()
        return api_response

    return req_handler_response

@app.route('/api/v1/event/<event_id>', methods=['GET'])
def get_event(event_id):
    """
        This is the endpoint returning a single event with the given id
    """
    req_handler_response = request_handler.validate_token(request)

    if req_handler_response['success']:
        core_app_context = req_handler_response['core_app_context']
        api_response = event_service.get_event(event_id)
        return api_response

    return req_handler_response

@app.route('/api/v1/event/insert', methods=['POST'])
def insert_event():
    """
        This is the endpoint for creating a new event
    """
    req_handler_response = request_handler.validate_token(request)

    if req_handler_response['success']:
        core_app_context = req_handler_response['core_app_context']
        data = request.get_json()
        api_response = event_service.insert_event(data, core_app_context)
        return api_response

    return req_handler_response

@app.route('/api/v1/event/delete/<event_id>', methods=['DELETE'])
def delete_event(event_id):
    """
        This is endpoint for deleting an event 
    """
    req_handler_response = request_handler.validate_token(request)

    if req_handler_response['success']:
        core_app_context = req_handler_response['core_app_context']
        api_response = event_service.delete_event(event_id)
        return api_response

    return req_handler_response

@app.route('/api/v1/event/update', methods=['PUT'])
def update_event():
    """
        This is endpoint for updating an event 
    """
    req_handler_response = request_handler.validate_token(request)

    if req_handler_response['success']:
        core_app_context = req_handler_response['core_app_context']
        data = request.get_json()        
        api_response = event_service.update_event(data)
        return api_response

    return req_handler_response

@app.route('/api/v1/event/my-events', methods=['GET'])
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

@app.route('/api/v1/event/<event_category_id>/events', methods=['GET'])
def get_event_cat_events(event_category_id):
    """
        This is an endpoint for fetching all events which belongs to the given
        event category id
    """
    req_handler_response = request_handler.validate_token(request)

    if req_handler_response['success']:
        core_app_context = req_handler_response['core_app_context']
        api_response = event_service.get_event_cat_events(event_category_id, core_app_context)
        return api_response

    return req_handler_response

@app.route('/api/v1/application/<event_id>/applications', methods=['GET'])
def get_event_applications(event_id):
    """
        This is an endpoint for fetching all applications which belongs to the given
        event id
    """
    req_handler_response = request_handler.validate_token(request)

    if req_handler_response['success']:
        core_app_context = req_handler_response['core_app_context']
        api_response = application_service.get_event_applications(event_id, core_app_context)
        return api_response

    return req_handler_response

@app.route('/api/v1/certificate/<event_id>/certificates', methods=['GET'])
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

if __name__ == '__main__':
    app.run()
