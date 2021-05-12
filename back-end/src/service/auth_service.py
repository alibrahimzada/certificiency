from service import Service
from data.models.auth import Auth

class AuthService(Service):

    def __init__(self):
        self.auth = Auth()

    def login(self, data):
        return self.auth.login(data)