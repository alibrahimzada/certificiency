from service import Service
from data.models.auth import Auth 
from service.helpers.crypto_helper import CryptoHelper

class AuthService(Service):

    def __init__(self):
        self.auth = Auth()
        self.crypto_helper = CryptoHelper()

    def login(self, data):
        return self.auth.login(data)