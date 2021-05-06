# from api import app
from service.userService import UserService
# from service.user import UserService
# put __init__.py files in each directory
from flask import jsonify, Blueprint

user_service = UserService()

bp = Blueprint('user', __name__)
@bp.route('', methods=['GET'])
def get_users():
    """
        This is the endpoint returning user list
    """
    users = user_service.get_users()

    return jsonify(users)



    