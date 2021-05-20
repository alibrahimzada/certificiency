from src.service import Service
from src.data.models.auth import Auth 
from src.service.helpers.crypto_helper import CryptoHelper

class AuthService(Service):

    def __init__(self):
        self.auth = Auth()
        self.crypto_helper = CryptoHelper()

    def login(self, data):
        encrypted_password = self.encrypt_password(data)
        data['password'] = encrypted_password
        return self.auth.login(data)

    def encrypt_password(self, data):
        encrypted_password = self.crypto_helper.sha256_encrypt(data['username'], data['password'])
        return encrypted_password
