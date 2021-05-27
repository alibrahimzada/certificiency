from __future__ import absolute_import
from flask import Flask, request
from src.service.auth_service import AuthService
from src.service.user_service import UserService
from src.service.role_service import RoleService
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
    # req_handler_response = request_handler.validate_token(request)

    # if req_handler_response['success']:
    #     core_app_context = req_handler_response['core_app_context']
    #     api_response = role_service.get_roles()
    #     return api_response

    api_response = role_service.get_roles()
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

@app.route('/api/v1/role', methods=['POST'])
def insert_role():
    """
        This is the endpoint for creating a new role
    """
    req_handler_response = request_handler.validate_token(request)

    if req_handler_response['success']:
        core_app_context = req_handler_response['core_app_context']
        data = request.get_json()
        api_response = role_service.insert_role(data)
        return api_response

    return req_handler_response

@app.route('/api/v1/role', methods=['DELETE'])
def delete_role():
    """
        This is endpoint for deleting a role 
    """
    req_handler_response = request_handler.validate_token(request)

    if req_handler_response['success']:
        core_app_context = req_handler_response['core_app_context']
        data = request.get_json()
        api_response = role_service.delete_role(data)
        return api_response

    return req_handler_response

# @app.route('/api/v1/role', methods=['PUT'])
# def update_user():
#     """
#         This is endpoint for updating a role
#     """
#     req_handler_response = request_handler.validate_token(request)

#     if req_handler_response['success']:
#         core_app_context = req_handler_response['core_app_context']
#         data = request.get_json()
#         api_response = role_service.update_role(data)
#         return api_response

#     return req_handler_response

if __name__ == '__main__':
    app.run()
