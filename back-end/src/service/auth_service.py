from src.service import Service
from src.data.models.auth import Auth 
from src.service.helpers.crypto_helper import CryptoHelper
from src.service.helpers.auth_helper import AuthHelper

class AuthService(Service):

    def __init__(self):
        self.auth = Auth()
        self.crypto_helper = CryptoHelper()
        self.auth_helper = AuthHelper()

    def login(self, data):
        encrypted_password = self.encrypt_password(data)
        data['password'] = encrypted_password

        api_response = self.auth.login(data)
        if api_response['success']:

            user_id = api_response['data']['user_id']
            customer_id = api_response['data']['customer_id']
            role_id = api_response['data']['role_id']

            jwt = self.auth_helper.encode_auth_token(user_id, customer_id, role_id)

            api_response['token'] = jwt.decode("utf-8")
            api_response['exp_in_mins'] = 480   # token expires in 8 hours
            return api_response
            
        return api_response

    def encrypt_password(self, data):
        encrypted_password = self.crypto_helper.sha256_encrypt(data['username'], data['password'])
        return encrypted_password
