from src.service import Service
from src.data.models.auth import Auth 
from src.service.helpers.crypto_helper import CryptoHelper

class AuthService(Service):

    def __init__(self):
        self.auth = Auth()
        self.crypto_helper = CryptoHelper()

    def login(self, data):
        return self.auth.login(data)