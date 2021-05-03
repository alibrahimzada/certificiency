from api import app
from core.controllers import Controller
# from service.user import UserService
# put __init__.py files in each directory
from flask import jsonify, Blueprint

bp = Blueprint('userController', __name__)

@bp.route('/api/v1/user', methods=['GET'])
def get_users():
    """
        This is the endpoint returning user list
    """
    print("Test")
    return jsonify([{'username': 'ali', 'email': 'ali@gmail.com'}])

# class UserController(Controller):

#     def __init__(self):
#         Controller.__init__()
#         # self.service = UserService()
#         pass


#     @bp.route('/api/v1/user', methods=['GET'])
#     def get_users(self):
#         """
#             This is the endpoint returning user list
#         """
#         print("Test")
#         return jsonify([{'username': 'ali', 'email': 'ali@gmail.com'}])