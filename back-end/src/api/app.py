from __future__ import absolute_import
from flask import Flask, request
from src.service.auth_service import AuthService
from src.service.user_service import UserService
# from flask_cors import CORS

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
    api_response = user_service.get_users()
    return api_response

if __name__ == '__main__':
    app.run()
