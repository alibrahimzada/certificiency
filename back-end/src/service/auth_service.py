from src.service import Service
from src.data.models.auth import Auth 
from src.service.helpers.crypto_helper import CryptoHelper
from flask_jwt import JWT
from werkzeug.security import safe_str_cmp
from src.api.app import app

class UserLogin():

    def __init__(self, id, name, password):
        self.id = id
        self.name = name
        self.password = password

class AuthService(Service):

    def __init__(self):
        self.auth = Auth()
        self.crypto_helper = CryptoHelper()
        self.username_table = {}
        self.userid_table = {}

    def login(self, data):
        encrypted_password = self.encrypt_password(data)
        data['password'] = encrypted_password

        api_response = self.auth.login(data)
        if api_response['success']:
            user_id = api_response['data']['user_id']
            user_name = api_response['data']['username']
            password = api_response['data']['password']

            user = UserLogin(user_id, user_name, password)
            self.username_table[user.name] = user
            self.userid_table[user.id] = user

            jwt = JWT(app, self.authenticate, self.identity)

            api_response['JWT'] = jwt

            return api_response
            
        return api_response

    def encrypt_password(self, data):
        encrypted_password = self.crypto_helper.sha256_encrypt(data['username'], data['password'])
        return encrypted_password

    def authenticate(self, username, password):
        user = self.username_table.get(username, None)
        if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
            return user

    def identity(self, payload):
        user_id = payload['identity']
        return self.userid_table.get(user_id, None)
