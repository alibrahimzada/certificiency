from ..service import Service
from src.data.models import User

class UserService(Service):

    def __init__(self):
        self.user = User()

    def getUsers(self):
        pass